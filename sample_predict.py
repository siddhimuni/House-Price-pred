import mlflow
import pandas as pd

# Input data for prediction
input_data = {
    "dataframe_records": [
        {
            "Order": 1,
            "PID": 5286,
            "MS SubClass": 20,
            "Lot Frontage": 80.0,
            "Lot Area": 9600,
            "Overall Qual": 5,
            "Overall Cond": 7,
            "Year Built": 1961,
            "Year Remod/Add": 1961,
            "Mas Vnr Area": 0.0,
            "BsmtFin SF 1": 700.0,
            "BsmtFin SF 2": 0.0,
            "Bsmt Unf SF": 150,
            "Total Bsmt SF": 850.0,
            "1st Flr SF": 856,
            "2nd Flr SF": 854,
            "Low Qual Fin SF": 0,
            "Gr Liv Area": 1710.0,
            "Bsmt Full Bath": 1,
            "Bsmt Half Bath": 0,
            "Full Bath": 1,
            "Half Bath": 0,
            "Bedroom AbvGr": 3,
            "Kitchen AbvGr": 1,
            "TotRms AbvGrd": 7,
            "Fireplaces": 2,
            "Garage Yr Blt": 1961,
            "Garage Cars": 2,
            "Garage Area": 500.0,
            "Wood Deck SF": 210.0,
            "Open Porch SF": 0,
            "Enclosed Porch": 0,
            "3Ssn Porch": 0,
            "Screen Porch": 0,
            "Pool Area": 0,
            "Misc Val": 0,
            "Mo Sold": 5,
            "Yr Sold": 2010
        }
    ]
}

# Convert input data to pandas DataFrame
input_df = pd.DataFrame(input_data["dataframe_records"])

# Path to the locally saved model
model_uri = "mlruns/0/d5e446b13e944857832f3d637211e09f/artifacts/model"  # Replace with the correct path

# Load the model using MLflow
loaded_model = mlflow.sklearn.load_model(model_uri)

# Generate predictions
predictions = loaded_model.predict(input_df)

# Print the predictions
print(f"Predictions: {predictions}")
