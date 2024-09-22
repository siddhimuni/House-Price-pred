import logging
import numpy as np
import pandas as pd
from zenml import step
from typing import Tuple
from src.data_splitter import DataSplitter, DataSplittingStrategy, SimpleTrainTestSplitStrategy


@step
def data_splitting_step(df:pd.DataFrame, target_column:str)-> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    splitter=DataSplitter(SimpleTrainTestSplitStrategy())
    X_train, X_test, y_train, y_test = splitter.split(df, target_column)
    return X_train, X_test, y_train, y_test