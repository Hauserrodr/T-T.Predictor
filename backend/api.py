import io
import numpy as np
import datetime
import pytz
import time
import shutil
import os
from pathlib import Path

import asyncio
from fastapi.responses import HTMLResponse, Response
from fastapi import FastAPI
from starlette.responses import FileResponse, StreamingResponse
from uvicorn import Config, Server

from loguru import logger

dir_path = Path(os.path.realpath(__file__)).parent

logger.add(os.path.join(dir_path,"logs","api.log"), level="TRACE", rotation="30 days")
logger.info("Logging started")

tz = pytz.timezone('America/Sao_Paulo')

app = FastAPI()

@app.get("/add_task")
async def add_task(task_name):
    return task_name


async def task_training_loop():
    """
    Creates an loop for automatic training using task database.
    """
    while True:
        if False:
            pass
            #If number of tasks > threshold
            #Train new model
        else:
            await asyncio.sleep(1)

if __name__ == "__main__":
    logger.info('Starting Task Predictor Backend API...')
    loop = asyncio.new_event_loop()
    config = Config(app=app, loop=loop, host="0.0.0.0", port=4242, reload=True)
    server = Server(config)
    loop.create_task(task_training_loop())
    loop.run_until_complete(server.serve())