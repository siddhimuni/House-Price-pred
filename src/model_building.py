import logging
from abc import ABC, abstractmethod
import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
        pass


class LinearRegressionModel(ModelBuildingStrategy):
    def build_and_train_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
        if not isinstance(X_train, pd.DataFrame):
            raise TypeError("X_train must be a dataframe")
        if not isinstance(y_train, pd.Series):
            raise TypeError("y_train must be a series")
        
        logging.info("Initializing Linear Regression model")
        
        pipeline = Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LinearRegression())
            ]
        )
        
        logging.info("Training Linear Regression model")
        pipeline.fit(X_train, y_train)
        logging.info("Model training completed")
        
        return pipeline


class ModelBuilder:
    def __init__(self, strategy: ModelBuildingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ModelBuildingStrategy):
        logging.info("Switching the model building strategy")
        self.strategy = strategy

    def build_model(self, X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
        return self.strategy.build_and_train_model(X_train, y_train)


if __name__ == "__main__":
    pass