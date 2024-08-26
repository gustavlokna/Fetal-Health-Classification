import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load your dataset
print("hei")

data = pd.read_csv('C:/Users/mathi/OneDrive/Dokumenter/Github/Prosjekt/Fetal-Health-Classification/Data/fetal_health.csv')

# Inspect the dataset
print(data.columns())
"""
# Split the data into features and target
X = data.drop(columns=['fetal_health'])  # Features (independent variables)
y = data['fetal_health']  # Target variable (what you want to predict)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

"""