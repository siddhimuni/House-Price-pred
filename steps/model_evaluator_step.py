import numpy as np
import pandas as pd
import logging
from src.model_evaluator import ModelEvaluationStrategy, RegressionModelEvaluationStrategy, ModelEvaluator
from zenml import step
from sklearn.pipeline import Pipeline

@step(enable_cache=False)
def model_evaluator_step(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series):
    model_evaluator = ModelEvaluator(RegressionModelEvaluationStrategy())
    evaluation_results = model_evaluator.evaluate(model, X_test, y_test)
    
    accuracy = evaluation_results["R2 score"]
    
    logging.info(f"Model accuracy (R2 score): {accuracy}")
    
    return accuracy