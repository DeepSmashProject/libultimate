from fastapi import FastAPI, status, HTTPException, Query
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json
from .controller import Controller
from .enums import Button
from typing import List, Optional, Tuple
from .util import encode_image

app = FastAPI(
    title="libultimate",
    docs_url="/docs",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],    
    allow_headers=["*"]     
)

class AddControllerRequest(BaseModel):
    player_id: int

@app.post("/controller/add")
async def add_controller(data: AddControllerRequest):
    controller = Controller(player_id=data.player_id)
    app.console.add_controller(controller)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})

class StickInput(BaseModel):
    stick_x: float
    stick_y: float

class OperateControllerRequest(BaseModel):
    player_id: int
    buttons: List[Button]
    main_stick: StickInput
    c_stick: StickInput
    hold: bool

@app.post("/controller/input")
async def send_controller_input(data: OperateControllerRequest):
    controller = app.console.get_controller(data.player_id)
    if controller:
        buttons = [Button(bt_value) for bt_value in data.buttons]
        controller.input(buttons, (data.main_stick.stick_x, data.main_stick.stick_y), (data.c_stick.stick_x, data.c_stick.stick_y), data.hold)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Controller not found")

@app.get("/stream/game_state")
async def stream_game_state(
    fps: Optional[int] = Query(default=10, ge=2, le=60, description="Frames per second"),
    include_image: Optional[bool] = Query(default=False, description="Include image in response"),
    image_size: Optional[str] = Query(default=None, description="Resize image to this size (e.g. 640x480)"),
):
    def generate():
        try:
            image_size_tuple = (int(image_size.split("x")[0]), int(image_size.split("x")[1])) if image_size else None
            for gamestate in app.console.stream(fps=fps, include_image=include_image, image_size=image_size_tuple):
                if gamestate.image is not None:
                    gamestate.image = encode_image(gamestate.image)
                yield json.dumps(gamestate.json())
        except Exception as err:
            return JSONResponse(status_code=500, content={"message": "Error: {}".format(err)})
    return StreamingResponse(generate(), media_type="application/json")

class UltimateServer:
    def __init__(self, console):
        app.console = console

    def run(self, address, port, log_level="info"):
        uvicorn.run(app, host=address, port=port, log_level=log_level)