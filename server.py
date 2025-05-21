import os
import time
import logging

from dotenv import load_dotenv

import uvicorn
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from auth.jwt_utils import validate_token
from etl.extractor import run_etl_process

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

load_dotenv()

app = FastAPI(root_path="/etl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)

@app.get("/execute")
def run(
    request: Request,
    response: Response
    ):

    start_time_service = time.time()
    logger.info("---- INVOKING ETL WITH PARAMS ---- ")

    token = request.headers.get("Authorization") or request.headers.get("authorization")

    if not token:
        raise HTTPException(status_code=401, detail="Token was not provided.")

    if not validate_token(token.replace("Bearer ", "")):
        raise HTTPException(status_code=401, detail="Invalid or expired token.")

    response_process = run_etl_process()

    end_time_service = time.time()

    total_time = f"{end_time_service - start_time_service:.3f}s"
    data_response = {"response": response_process, "token": token, "total_time": total_time}

    logger.info("--- Logging Response ---")
    logger.info(
        "\nResponse: %s\nToken: %s\nTotal Time: %s",
        data_response["response"],
        data_response["token"],
        data_response["total_time"],
    )

    # CORS headers
    response.headers["Access-Control-Allow-Origin"] = (
        "*"  # TODO make it more restrictive for production environments
    )
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
    return data_response

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger.info("-- STARTING SERVER WITH GUNICORN --")
    port = int(os.getenv("APP_PORT", 8000))
    uvicorn.run("server:app", host="127.0.0.1", port=port, reload=True)
