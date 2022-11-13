from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import time
import json
from .console import Console
from .controller import Controller
from .enums import Button
from typing import List, Tuple

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

@app.post("/controller")
async def add_controller(data: AddControllerRequest):
    controller = Controller(player_id=data.player_id)
    app.console.add_controller(controller)

class StickInput(BaseModel):
    stick_x: float
    stick_y: float

class OperateControllerRequest(BaseModel):
    player_id: int
    buttons: List[Button]
    main_stick: StickInput
    c_stick: StickInput
    hold: bool

@app.post("/operate")
async def operate(data: OperateControllerRequest):
    controller = app.console.get_controller(data.player_id)
    buttons = [Button(bt_value) for bt_value in data.buttons]
    controller.input(buttons, (data.main_stick.stick_x, data.main_stick.stick_y), (data.c_stick.stick_x, data.c_stick.stick_y), data.hold)

@app.get("/stream/game_state")
async def stream_game_state():
    def generate():
        try:
            for gamestate in app.console.stream(fps=app.config.fps):
                yield json.dumps(gamestate.json())
        except Exception as err:
            print('error', err)
            return JSONResponse(status_code=500, content={"message": "Error: {}".format(err)})
    return StreamingResponse(generate(), media_type="application/json")

class UltimateServerConfig(BaseModel):
    fps: int

class UltimateServer:
    def __init__(self, console, config: UltimateServerConfig):
        app.console = console
        app.config = config

    def run(self, address, port, log_level="info"):
        uvicorn.run(app, host=address, port=port, log_level=log_level)