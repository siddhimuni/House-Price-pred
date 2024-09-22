import numpy as np
import pandas as pd
import logging
from src.model_building import ModelBuilder, LinearRegressionModel, ModelBuildingStrategy
from zenml import step
from sklearn.pipeline import Pipeline
import mlflow

@step(enable_cache=False)
def model_building_step(X_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    model = ModelBuilder(LinearRegressionModel())
    pipeline = model.build_model(X_train, y_train)
    
    # Ensure we're returning a Pipeline object
    if not isinstance(pipeline, Pipeline):
        raise TypeError(f"Expected a Pipeline object, but got {type(pipeline)}")
    with mlflow.start_run() as run:
        # Log the entire pipeline
        mlflow.sklearn.log_model(pipeline, "model")
        print(f"Model pipeline logged to MLFlow under run ID: {run.info.run_id}")
        
        # You can also log other parameters or metrics here, if applicable
        mlflow.log_param("model_type", "LinearRegression")
    
    return pipeline
    