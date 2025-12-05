import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
dataframe = pd.DataFrame(df)

#print(df.head())
#print(df.info())

''' print("Veriseti boyutu: ", df.shape)
print("Sütunlar: ",df.columns.tolist())
print("Eksik veri sayısı:",df.isna().sum())
print("Veri türleri: ",df.dtypes) '''

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")
print(df.isna().sum())

print(df["type"].value_counts())

