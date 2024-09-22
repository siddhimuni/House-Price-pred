import numpy as np
import pandas as pd
import logging
from zenml import step
from src.outlier_detection import OutlierDetectionStrategy, OutlierDetector, ZScoreOutlierDetection, IQROutlierDetection

@step
def outlier_detection_step(df:pd.DataFrame, features: str):
    logging.info("Starting outlier detection: ")

    if df is None:
        logging.error("Received a NoneType dataframe")
        raise ValueError("Input df must be a non-null pandas dataframe")
    
    if not isinstance(df, pd.DataFrame):
        logging.error(f"Expected pandas dataframe, got {type(df)}")
        raise ValueError("Input df must be of pandas dataframe")
    
    if features not in df.columns:
        logging.error(f"Column: {features} does not exist in data columns")
        raise ValueError(f"Column {features} does not exist")
    df_numeric = df.select_dtypes(include=[int, float])

    outlier_detector = OutlierDetector(ZScoreOutlierDetection(threshold=3))
    outliers = outlier_detector.detect_outliers(df_numeric)
    df_cleaned = outlier_detector.handle_outliers(df_numeric, method="remove")
    return df_cleaned

