import os
import sys
import time

# Get the current directory (root of the project)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the project root (parent directory of the current file)
project_root = os.path.dirname(current_dir)

# Add the project root to the Python path
sys.path.append(project_root)

from zenml import pipeline
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)
from pipelines.training_pipeline import ml_pipeline
from steps.dynamic_importer import dynamic_importer
from steps.prediction_service_loader import prediction_service_loader
from steps.predictor import predictor

from zenml import pipeline, step
from zenml.steps import Output
import pandas as pd

@step
def get_deploy_decision(accuracy: float) -> bool:
    """
    Determine whether to deploy the model or not.
    """
    decision = accuracy > 0.5  # Adjust threshold as needed
    print(f"Accuracy: {accuracy}, Deployment Decision: {decision}")
    return decision

@pipeline
def continuous_deployment_pipeline(file_path: str):
    model, accuracy = ml_pipeline(file_path)
    deploy_decision = get_deploy_decision(accuracy)
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deploy_decision,
        workers=3,
    )

@pipeline
def inference_pipeline():
    batch_data = dynamic_importer()
    model_deployment_service = prediction_service_loader(
        pipeline_name="continuous_deployment_pipeline",
        step_name="mlflow_model_deployer_step",
        
    )
    predictor(service=model_deployment_service, input_data=batch_data)

