import sys
import os

# Get the current directory (root of the project)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the project root (parent directory of the current file)
project_root = os.path.dirname(current_dir)

# Add the project root to the Python path
sys.path.append(project_root)
from pipelines.training_pipeline import ml_pipeline


if __name__=="__main__":
    ml_pipeline(file_path="C:/Users/siddh/OneDrive/Desktop/Projects/End-to-end House price pred/Data/AmesHousing.zip")