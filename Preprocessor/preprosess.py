import pandas as pd 
import numpy as np 
from utils.loader import load_data

def data_preprocessing( data_config: dict) -> pd.DataFrame:
    data = load_data(data_config["data"]["raw"])
    return  data