import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
from utils.loader import load_data

def train_model(data_config: dict) -> None:
    # Load the data
    data = load_data(data_config["data"]["trained"])
    
    # Splitting the data into features and target
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1]   # Target

    # Determine the output directory based on the detector_type
    base_output_dir = data_config["model"]["output_dir"]
    detector_type = data_config["model"]["detector_type"]
    output_dir = os.path.join(base_output_dir, detector_type)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Define the path to save the trained model
    model_path = os.path.join(output_dir, 'trained_model.pkl')

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    # Save the trained model to the specified path
    joblib.dump(model, model_path)

    print(f"Model trained and saved to {model_path}")
