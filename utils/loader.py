import os
import re
from collections import defaultdict

import joblib
import pandas as pd

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


def save_data(data: pd.DataFrame, file_path: str):
    """Save the processed data to a CSV file.

    Parameters
    ----------
    data : pd.DataFrame
        Processed data.
    file_path : str
        Path to save the CSV file.
    """
    # Sanitize the file path
    file_path = sanitize_file_path(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    data.to_csv(file_path, index=False)

def translate_norwegian_chars(file_path: str) -> str:
    """Translate Norwegian characters to English equivalents.

    Parameters
    ----------
    file_path : str
        Original file path.

    Returns
    -------
    str
        File path with Norwegian characters translated to English.
    """
    translations = {"æ": "ae", "ø": "oe", "å": "aa", "Æ": "Ae", "Ø": "Oe", "Å": "Aa"}
    for nor_char, eng_char in translations.items():
        file_path = file_path.replace(nor_char, eng_char)
    return file_path


def sanitize_file_path(file_path: str) -> str:
    """Sanitize the file path to use forward slashes and
    contain only English alphabets and no spaces.

    Parameters
    ----------
    file_path : str
        Original file path.

    Returns
    -------
    str
        Sanitized file path.
    """
    file_path = translate_norwegian_chars(file_path)
    file_path = file_path.replace("\\", "/")
    file_path = re.sub(r"[^A-Za-z0-9_./]", "", file_path)
    file_path = file_path.replace(" ", "")
    return file_path

