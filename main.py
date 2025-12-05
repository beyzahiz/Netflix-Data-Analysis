import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
df.isna().sum()

df["type"].value_counts()

fdsayisi= df["type"].value_counts()
fdsayisi.plot(kind="bar")
#plt.title("Film vs TV Show Sayıları")
#plt.show()

turler = df["listed_in"]
turler = turler.str.split(",") #virgül ile türleri ayırdım
turler = turler.explode() #alt alta yazıldı
print(turler.value_counts().head(10))

