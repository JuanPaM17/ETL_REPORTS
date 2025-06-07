import logging
from etl.extractor import run_etl_process

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    result = run_etl_process()
    if result:
        print("true")
    else:
        print("false")
