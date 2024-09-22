import click
from deployment_pipeline import (
    continuous_deployment_pipeline,
    inference_pipeline
)

from rich import print
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer

@click.command()

@click.option(
    "--stop-service",
    is_flag=True,
    default=False,
    help="Stop the prediction service when done"
)

@click.option(
    "--file-path",  # Add a file-path option to pass the training data
    required=True,  # Make this required
    help="File path for the training data"
)

def run_main(stop_service: bool, file_path: str):
    model_name = "prices_predictor"

    if stop_service:
        model_deployer = MLFlowModelDeployer.get_active_model_deployer()

        existing_services = model_deployer.find_model_server(
            pipeline_name="continuous_deployment_pipeline",
            pipeline_step_name="mlflow_model_deployer_step",
            model_name=model_name,
            running=True
        )

        if existing_services:
            existing_services[0].stop(timeout=10)
        return
    
    # Pass file_path to the pipeline
    continuous_deployment_pipeline(file_path)

    model_deployer = MLFlowModelDeployer.get_active_model_deployer()
    service = model_deployer.find_model_server(
        pipeline_name="continuous_deployment_pipeline",
        pipeline_step_name="mlflow_model_deployer_step",
        model_name=model_name
    )

    if service and service[0]:  # Ensure there is a running service
        print(f"MLFlow prediction server is running at {service[0].prediction_url}")
    else:
        print("No running prediction service found. Deployment might have failed.")
    inference_pipeline()

    print(
        f"ML Flow UI is available at -- backend-store-uri {get_tracking_uri()}"
    )

    service = model_deployer.find_model_server(
        pipeline_name="continuous_deployment_pipeline",
        pipeline_step_name="mlflow_model_deployer_step",
    )

    if service and service[0]:  # Check if service exists and is not empty
        print(
            f"The ML Flow prediction server is running locally and can process "
            f"and accept inference requests at:\n"
            f"{service[0].prediction_url}"
        )
    else:
        print("No running ML Flow prediction service was found.")


if __name__ == "__main__":
    run_main()
