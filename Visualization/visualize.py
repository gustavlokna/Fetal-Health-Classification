import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_matrix_make_png(data: pd.DataFrame, fileName: str) -> None:
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
    plt.savefig(f'../output/{fileName}', format='png', dpi=300, bbox_inches='tight')
    plt.show()

