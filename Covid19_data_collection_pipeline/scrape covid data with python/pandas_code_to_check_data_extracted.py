import pandas as pd

df=pd.read_csv("covid19.csv")
print("Here the shape of the dataset")
print(df.shape)
print("Now the first 5 rows")
print(df.head())
print("Now the last 5 rows")
print(df.tail())
