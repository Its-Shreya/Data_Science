import numpy as np
import pandas as pd
df11= pd.read_csv('Q1_data1.txt', header=None,sep=',')
df11
df11.isnull()
df11.isnull().any()
df11.dropna()

df=pd.read_csv("Q2_bollywood.csv")
df

df.info()
df.describe()
x=df.shape
x
df.head(10)
df.tail(10)
df['Genre'].value_counts()
df['Genre'].value_counts(normalize=True)
df['Genre'].value_counts().sort_values(ascending=True)
df['Budget'].value_counts().sort_values(ascending=False)
df[['Budget','BoxOfficeCollection','MovieName']].sort_values('BoxOfficeCollection',ascending=False)[0:5]
df.iloc[4:9,1:5]
df['Square_root_Budget']=df['Budget'].apply(np.sqrt)
df