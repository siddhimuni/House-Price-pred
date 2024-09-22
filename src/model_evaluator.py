import numpy as np
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.base import RegressorMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class ModelEvaluationStrategy(ABC):
    @abstractmethod
    def evaluate_model(self, model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
        pass

class RegressionModelEvaluationStrategy(ModelEvaluationStrategy):
    def evaluate_model(self, model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
        if not isinstance(X_test, pd.DataFrame):
            raise TypeError("X_test must be a dataframe")
        if not isinstance(y_test, pd.Series):
            raise TypeError("y_test must be a series")
        
        logging.info("Evaluating Regression model")

        logging.info("Predicting using the trained model")
        y_pred = model.predict(X_test)

        logging.info("Calculating evaluation metrics:")
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        metrics = {"Mean squared error": mse, "R2 score": r2}

        logging.info(f"Evaluation metrics: {metrics}")
        return metrics

class ModelEvaluator:
    def __init__(self, strategy: ModelEvaluationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ModelEvaluationStrategy):
        logging.info("Switching the model evaluation strategy")
        self.strategy = strategy

    def evaluate(self, model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series):
        logging.info("Evaluating the model using the selected strategy")
        return self.strategy.evaluate_model(model, X_test, y_test)