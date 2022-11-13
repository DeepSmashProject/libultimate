from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, StreamingResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import time
import json

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

@app.post("/operate_controller")
async def operate_controller():
    pass

@app.get("/stream/game_state")
async def stream_game_state():
    fps = 1
    def generate():
        try:
            while True:
                time.sleep(1/fps)
                yield json.dumps({"test": "test"})
        except GeneratorExit:
            print('closed')
        except Exception as err:
            print('error', err)
            return JSONResponse(status_code=500, content={"message": "Error: {}".format(err)})
    return StreamingResponse(generate(), media_type="application/json")


def run_server(address, port, log_level="info"):
    uvicorn.run(app, host=address, port=port, log_level=log_level)
