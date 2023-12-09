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

Q1=df['YoutubeViews'].quantile(0.25)
Q3=df['YoutubeViews'].quantile(0.75)
Q2=df['YoutubeViews'].median()
IQR=Q3-Q1
lower_whisker= Q1- 1.5*IQR
upper_whisker= Q3+ 1.5*IQR
outlier=df[(df['YoutubeViews']>upper_whisker)|(df['YoutubeViews']<lower_whisker)]
outlier

outlier.index
df.drop([28, 43, 89, 91, 92, 119],axis=0,inplace=True)
df.head()
sns.heatmap(df.corr(),annot=True)