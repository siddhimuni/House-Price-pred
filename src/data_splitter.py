import numpy as np
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.model_selection import train_test_split as tts


class DataSplittingStrategy(ABC):
    @abstractmethod
    def split_data(self, df: pd.DataFrame, target_column: str):
        pass


class SimpleTrainTestSplitStrategy(DataSplittingStrategy):
    def __init__(self, test_size=0.2, random_state=42):
        self.test_size=test_size
        self.random_state=random_state

    def split_data(self, df: pd.DataFrame, target_column: str):
        logging.info("Performing simple train-test split")
        X=df.drop(columns=[target_column])
        y=df[target_column]

        X_train,X_test,y_train,y_test = tts(X,y,test_size=self.test_size, random_state=self.random_state)
        logging.info("Train-test split completed") 
        return X_train,X_test,y_train,y_test
    


class DataSplitter:
    def __init__(self, strategy: DataSplittingStrategy):
        self.strategy=strategy
    def set_strategy(self, strategy : DataSplittingStrategy):
        logging.info("Switching data split strategy")
        self.strategy=strategy
    def split(self, df:pd.DataFrame,target_column: str ):
        logging.info("Splitting data using selected strategy")
        return self.strategy.split_data(df, target_column)
    


if __name__=="__main__":
    pass

        