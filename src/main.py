"""
Netflix Veri Analizi Projesi
Bu script Netflix veri seti üzerinde veri temizleme, dönüştürme ve görselleştirme işlemlerini içerir.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/netflix_titles.csv")
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
plt.figure(figsize=(10,5))
fdsayisi.plot(kind="bar")
plt.title("Film vs TV Show Sayıları")
plt.savefig("images/film_vs_tv.png")
plt.show()

turler = df["listed_in"]
turler = turler.str.split(",") #virgül ile türleri ayırdım
turler = turler.explode() #alt alta yazıldı
print(turler.value_counts().head(10))

on = turler.value_counts().head(10)
plt.figure(figsize=(10,5))
on.plot(kind="bar")
plt.title("Netflix'te En Popüler 10 Tür")
plt.savefig("images/top_10_genres.png")
plt.show()

ulke = df["country"]
ulke = ulke.str.split(",")
ulke = ulke.explode()
ulke = ulke.str.strip()  #baştaki ve sondaki boşlukları temizledim
print(ulke.value_counts().head(10))

ulkeOn = ulke.value_counts().head(10)
plt.figure(figsize=(10,5)) #yeni figure oluşturur eskiyi temizler
ulkeOn.plot(kind="bar")
plt.title("Netflix'te En Çok İçerik Üreten 10 Ülke")
plt.savefig("images/top_ulkeler.png")
plt.show()

#Yıllara göre içerik trendleri
yillar = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(12,5))
yillar.plot(kind="line")
plt.title("Yıllara Göre Netflix İçerik Üretimi")
plt.xlabel("Yıl")
plt.ylabel("İçerik Sayısı")
plt.savefig("images/yillara_gore_icerik_uretimi.png")
plt.show()

#İçerik süresi analizi
filmler = df[df["type"] == "Movie"] #filmler seçilir
filmler_temiz = filmler[filmler["duration"] != "Unknown"].copy() #unknown olanlar çıkarılır
filmler_temiz.loc[:,"duration_clean"] = (
    filmler_temiz["duration"].str.replace(" min", "").astype(int)
) #min silinir ve inte çevrilir
print(filmler_temiz[["duration", "duration_clean"]].head(10))

print("Ortalama film süresi:",filmler_temiz["duration_clean"].mean())
print("En kısa film süresi:", filmler_temiz["duration_clean"].min())
print("En uzun film süresi: ",filmler_temiz["duration_clean"].max())

plt.figure(figsize=(10,5))
filmler_temiz["duration_clean"].plot(kind="hist")
plt.title("Netflix Film Süresi Dağılımı")
plt.xlabel("Film Süresi(Dakika)")
plt.ylabel("Frekans")
plt.savefig("images/film_duration_hist.png")
plt.show()

diziler = df[df["type"]== "TV Show"]
diziler["duration"].head(20)
diziler_temiz = diziler["duration"].str.replace(" Seasons", "").str.replace(" Season", "").astype(int)
print(diziler_temiz.head(10))

print("Ortalama dizi sezon süresi: ",diziler_temiz.mean())
print("En kısa dizi sezon süresi: ",diziler_temiz.min())
print("En uzun dizi sezon süresi: ",diziler_temiz.max())

plt.figure(figsize=(10,5))
diziler_temiz.plot(kind="hist", color="purple")
plt.title("Netflix Dizilerinde Sezon Sayısı Dağılımı")
plt.xlabel("Sezon Sayısı")
plt.ylabel("Dizi Sayısı")
plt.savefig("images/tv_show_season_hist.png")
plt.show()