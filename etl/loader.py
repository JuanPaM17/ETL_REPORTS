import logging

logger = logging.getLogger(__name__)

def load_data(details_df, summary_df):
    from etl.config import dest_engine
    details_df.to_sql('order_details_summary', con=dest_engine, if_exists='replace', index=False)
    summary_df.to_sql('orders_summary', con=dest_engine, if_exists='replace', index=False)
    logger.info("Datos cargados correctamente en etl_dashboard")