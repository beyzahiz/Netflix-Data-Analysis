import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
dataframe = pd.DataFrame(df)

#print(df.head())
print(df.info())

print("Veriseti boyutu: ", df.shape)
print("Sütunlar: ",df.columns.tolist())
print("Eksik veri sayısı:",df.isna().sum())
print("Veri türleri: ",df.dtypes)

