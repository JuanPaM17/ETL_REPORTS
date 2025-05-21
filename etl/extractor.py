import logging
import pandas as pd
from etl.config import source_engine
from etl.query import QUERY
from etl.transformer import transform_data
from etl.loader import load_data

logger = logging.getLogger(__name__)

def run_etl_process():
    try:
        df = pd.read_sql(QUERY, con=source_engine)
        details_df, summary_df = transform_data(df)
        load_data(details_df, summary_df)
        return True
    except Exception as e:
        logger.info(f"Error en el proceso ETL: {e}")
        return False
