import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from utils.loader import load_data
from sklearn.metrics import mean_squared_error, r2_score

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

def predict_model(data_config: dict) -> None:
    # Load model
    base_output_dir = data_config["model"]["output_dir"]
    detector_type = data_config["model"]["detector_type"]
    output_dir = os.path.join(base_output_dir, detector_type)

    # Construct the path to the trained model
    model_path = os.path.join(output_dir, 'trained_model.pkl')
    model = joblib.load(model_path)

    # Load test data
    data = load_data(data_config["data"]["eval"])

    # Split the test data into features and target
    X_eval = data.iloc[:, :-1]  # All columns except the last one
    y_eval = data.iloc[:, -1]   # Only the last column

    y_pred = model.predict(X_eval)
    # Round predictions to the nearest whole number
    y_pred_rounded = np.round(y_pred)  # Round to nearest whole number
    y_pred_clamped = np.clip(y_pred_rounded, 1, 3)  # Clamp values between 1 and 3
    # Evaluate the model using clamped predictions
    mse = mean_squared_error(y_eval, y_pred_clamped)
    r2 = r2_score(y_eval, y_pred_clamped)

    # Print evaluation results
    print(f"Mean Squared Error on Test Data: {mse}")
    print(f"R-squared on Test Data: {r2}")
    #print(f"Rounded Predictions: {y_pred_rounded}")


def eval_plot(data_config: dict) -> None:
    # Load model
    base_output_dir = data_config["model"]["output_dir"]
    detector_type = data_config["model"]["detector_type"]
    output_dir = os.path.join(base_output_dir, detector_type)

    # Construct the path to the trained model
    model_path = os.path.join(output_dir, 'trained_model.pkl')
    model = joblib.load(model_path)

    # Load test data
    data = load_data(data_config["data"]["eval"])

    # Split the test data into features and target
    X_eval = data.iloc[:, :-1]  # All columns except the last one
    y_eval = data.iloc[:, -1]   # Only the last column

    # Predict using the loaded model
    y_pred = model.predict(X_eval)

    # Round predictions to the nearest whole number and clamp between 1 and 3
    y_pred_rounded = np.round(y_pred)  # Round to nearest whole number
    y_pred_clamped = np.clip(y_pred_rounded, 1, 3)  # Clamp values between 1 and 3

    # Create a DataFrame for plotting
    eval_df = pd.DataFrame({'Actual': y_eval, 'Predicted': y_pred_clamped})

    # Create box plots
    plt.figure(figsize=(8, 6))
    eval_df.boxplot(by='Predicted', column='Actual', grid=False, showfliers=False)
    plt.title('Actual vs Predicted Values')
    plt.suptitle('')  # Remove the default suptitle to avoid overlap
    plt.xlabel('Predicted Value')
    plt.ylabel('Actual Value')
    plt.ylim(0, 4)  # Set y-axis limits for clarity
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gca().set_facecolor('whitesmoke')

    # Make the boxes a little see-through
    for patch in plt.gca().artists:
        patch.set_alpha(0.6)

    # Save the plot
    plot_dir = data_config["Output"]["eval"]  # Corrected key access
    os.makedirs(plot_dir, exist_ok=True)  # Ensure the plot directory exists
    plot_path = os.path.join(plot_dir, 'eval_plot.png')
    plt.savefig(plot_path, bbox_inches='tight')
    plt.close()

    print(f"Evaluation plot saved to {plot_path}")