import os
from sqlalchemy import create_engine

from dotenv import load_dotenv
load_dotenv()


SOURCE_DB_URL = os.getenv("SOURCE_DB_URL")
DEST_DB_URL = os.getenv("DEST_DB_URL")

source_engine = create_engine(SOURCE_DB_URL)
dest_engine = create_engine(DEST_DB_URL)
