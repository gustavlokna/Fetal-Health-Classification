import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.loader import load_data

def correlation_matrix_make_png(fileName: str, data_config: dict) -> None: 
    data = load_data(data_config["data"]["raw"])
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
    savePath = f"{data_config['Output']['correlation_matrix']}.png"
    print(savePath)
    plt.savefig(savePath, format='png', dpi=300, bbox_inches='tight')

