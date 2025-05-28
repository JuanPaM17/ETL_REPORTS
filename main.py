# main.py
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
from etl.extractor import run_etl_process

app = FastAPI(root_path="/etl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8082"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)

@app.get("/execute")
def run(request: Request, response: Response):
    start_time_service = time.time()
    logger.info("---- INVOKING ETL WITH PARAMS ----")

    response_process = run_etl_process()

    end_time_service = time.time()
    total_time = f"{end_time_service - start_time_service:.3f}s"
    data_response = {"response": response_process, "total_time": total_time}

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"

    return data_response
