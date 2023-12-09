import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('Q2_bollywood.csv')
df.head()

def day_extraction(i):
    return i.split('-')[0]
def month_extract(i):
    return i.split('-')[1]
df['Date']=df['Release Date'].apply(day_extraction)
df['Month']=df['Release Date'].apply(month_extract)
df

df.groupby(['Month','Genre'])['BoxOfficeCollection'].mean()
df[df['BoxOfficeCollection']>100]
df.drop('SlNo', inplace=True,axis=1)

plt.figure(figsize=(10, 5))
plt.bar(df['BoxOfficeCollection'], df['Budget'], color='red', label='Bar Chart')
plt.xlabel('BoxOfficeCollection')
plt.ylabel('Budget')
plt.title('Bar Chart Example')
plt.legend()
plt.show()

df['YoutubeViews']
df.boxplot('YoutubeViews')
sns.pairplot(df)
sns.boxplot(df['YoutubeViews'])

plt.figure(figsize=(10,7))
plt.scatter(df['YoutubeViews'], df['Budget'], c='red')
plt.xlabel('YoutubeViews')
plt.ylabel('Budget')
plt.show()