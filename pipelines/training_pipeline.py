import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (which contains the 'steps' folder)
project_root = os.path.dirname(current_dir)

# Add the project root to the Python path
sys.path.append(project_root)

# Optionally, you can also add the 'src' directory if needed
src_dir = os.path.join(project_root, 'src')
sys.path.append(src_dir)

from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_value_step import handle_missing_value_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_splitting_step import data_splitting_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step
import zenml
import mlflow
from zenml import step, pipeline, Model
from steps.mlflow_model_deployer_step import mlflow_model_deployer_step

@pipeline(
    model = Model(
        name="prices_predictor"
    )
)


def ml_pipeline(file_path: str):

    raw_data= data_ingestion_step(
        file_path="C:/Users/siddh/OneDrive/Desktop/Projects/End-to-end House price pred/Data/AmesHousing.zip"
    )


    filled_data = handle_missing_value_step(raw_data)

    engineered_data = feature_engineering_step(filled_data, strategy="Log", features= ["Gr Liv Area" , "SalePrice"])
    clean_data = outlier_detection_step(engineered_data , features ="SalePrice" )

    X_train,X_test,y_train,y_test=data_splitting_step(clean_data, target_column='SalePrice')

    model = model_building_step( X_train, y_train)
    accuracy = model_evaluator_step(model, X_test, y_test)
   
    return model, accuracy
    


if __name__=="__main__":
    run = ml_pipeline()




