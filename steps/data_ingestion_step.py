import pandas as pd
from zenml import step
from src.ingest_data import DataIngestorFactory


@step
def data_ingestion_step(file_path = str) -> pd.DataFrame:
    file_extension=".zip"
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    df = data_ingestor.ingest(file_path)
    return df