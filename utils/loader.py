import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """Load the sensor data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the sensor data CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")

    return pd.read_csv(file_path)
