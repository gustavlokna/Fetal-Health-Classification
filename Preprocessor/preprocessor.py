import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from utils.loader import load_data
import os

def data_preprocessing(data_config: dict) -> None:
    # Load the data
    data = load_data(data_config["data"]["raw"])
    
    # Drop any missing values
    data = data.dropna()

    # Print the columns
    print(data.columns)

    # Splitting the data into features and target
    X = data.iloc[:, :-1]  # Features
    y = data.iloc[:, -1]   # Target

    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Combine the scaled features and target into a single DataFrame
    scaled_data = pd.DataFrame(X_scaled, columns=X.columns)
    scaled_data['target'] = y.reset_index(drop=True)  # Adjust column name if necessary

    # Split the data into training and evaluation sets
    train_data, eval_data = train_test_split(scaled_data, test_size=0.2, random_state=42)

    # Save the processed data
    processed_folder = data_config["data"]["processed"]
    
    # Create the directory if it doesn't exist
    os.makedirs(processed_folder, exist_ok=True)
    
    # Save the training and evaluation data to separate files
    train_data.to_csv(f"{processed_folder}/train.csv", index=False)
    eval_data.to_csv(f"{processed_folder}/eval.csv", index=False)

    print("Data processing complete. Files saved to:", processed_folder)