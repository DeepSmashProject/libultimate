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

class OperateControllerRequest(BaseModel):
    player_id: int
    buttons: List[Button]
    main_stick: Tuple[float, float]
    c_stick: Tuple[float, float]
    hold: bool

@app.post("/operate")
async def operate(data: OperateControllerRequest):
    controller = app.console.get_controller(data.player_id)
    controller.input(data.buttons, data.main_stick, data.c_stick, data.hold)

@app.get("/stream/game_state")
async def stream_game_state():
    def generate():
        try:
            for gamestate in app.console.stream(fps=app.config.fps):
                yield json.dumps(gamestate)
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
