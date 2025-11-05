import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
dataframe = pd.DataFrame(df)

print(df.head())
print(df.info())