# importing pandas for data cleaning.
import pandas as pd



df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()

#Casting Release_Date column and extracing year values

# casting column a
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
# confirming changes
print(df['Release_Date'].dtypes)

df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes

df.info()

#Dropping Overview, Original_Languege and Poster-Url
# making list of column to be dropped

cols = ['Overview', 'Original_Language', 'Poster_Url']

# dropping columns and confirming changes
df.drop(cols, axis = 1, inplace = True)
df.columns
df.head()