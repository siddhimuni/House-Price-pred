import numpy as np
import pandas as pd
from src.feature_engineering import FeatureEngineer, FeatureEngineering, MinMaxScaling, StandardScaling, LogTransformation, OneHotEncoding
from zenml import step

@step
def feature_engineering_step(df: pd.DataFrame, strategy : str ="Log", features :list = None) -> pd.DataFrame:
    if features is None:
        features=[]
    if strategy=="Log":
        engineer = FeatureEngineer(LogTransformation(features))
    elif strategy=="Standard_scaling":
        engineer = FeatureEngineer(StandardScaling(features))
    elif strategy == "Min_max_scaling":
        engineer = FeatureEngineer(MinMaxScaling(features))
    elif strategy=="One_hot_encoding":
        engineer = FeatureEngineer(OneHotEncoding(features))
    else:
        raise ValueError(f"Unsupoorted feature engineering strategy : {strategy}")
    
    transformed_df = engineer.apply_feature_engineering(df)
    return transformed_df
