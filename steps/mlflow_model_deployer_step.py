from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer
from zenml import step

@step(enable_cache=False)
def mlflow_model_deployer_step(model, deploy_decision: bool):
    if deploy_decision:
        model_deployer = MLFlowModelDeployer.get_active_model_deployer()
        service = model_deployer.deploy_model(model)
        if service:
            print(f"Model deployed successfully at: {service.prediction_url}")
        else:
            print("Model deployment failed or service not returned.")
        
        return service
    else:
        print("Model not deployed due to insufficient accuracy.")
