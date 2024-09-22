import logging
import pandas as pd
from abc import ABC, abstractmethod


logging.basicConfig(level=logging.INFO)


class MissingValueHandlingStrategy(ABC):

    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class DropMissingValueStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=0, thresh=None):
        self.axis=axis
        self.thresh=thresh


    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        
        logging.info(f"Dropping missing values with axis={ self.axis} and threshold= {self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logging.info("Missing values dropped")
        return df_cleaned
    

class FillMissingValueStrategy(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None):
        self.method=method
        self.fill_value=fill_value


    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Filling missing values using method {self.method}")


        df_cleaned=df.copy()
        if self.method=="mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mean())
        elif self.method=="median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].median())
        elif self.method=="mode":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(df_cleaned[numeric_columns].mode())
        elif self.method=="constant":
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            logging.warning(f"Unknown method: {self.method}. No missing values handled")
        
        logging.info("Missing values filled")
        return df_cleaned


class MissingValueHandler:
    def __init__(self, strategy : MissingValueHandlingStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        logging.info("Switching missing value handling strategy")
        self.strategy=strategy
    def handle_missing_values(self, df:pd.DataFrame) -> pd.DataFrame:
        logging.info("Executing missing value handling strategy")
        return self.strategy.handle(df)
    
if __name__=="__main__":
    pass
