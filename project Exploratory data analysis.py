# importing lib.
import pandas as pd


df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()



# categorizing Vote_Average column
# We would cut the Vote_Average values and make 4 categories: popular average 
# below_avg not_popular to describe it more using catigorize_col() function
# provided above




def catigorize_col (df, col, labels):
 """
 catigorizes a certain column based on its quartiles
 
 Args:
 (df) df - dataframe we are proccesing
 (col) str - to be catigorized column's name 
 (labels) list - list of labels from min to max
 
 Returns:
 (df) df - dataframe with the categorized col
 """
 
 # setting the edges to cut the column accordingly
 edges = [df[col].describe()['min'],
 df[col].describe()['25%'],
 df[col].describe()['50%'],
 df[col].describe()['75%'],
 df[col].describe()['max']] 
 df[col] = pd.cut(df[col], edges, labels = labels, duplicates='drop')
 return df
# define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']
# categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)
# confirming changes
df['Vote_Average'].unique()

 #exploring column
df['Vote_Average'].value_counts()

 #dropping NaNs
df.dropna(inplace = True)
# confirming
df.isna().sum()

df.head()

# we'd split genres into a list and then
# explode our dataframe to have only one
# genre per row for ezch movie


# split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')
# explode the lists
df = df.explode('Genre').reset_index(drop=True)
df.head()

# casting column into category
df['Genre'] = df['Genre'].astype('category')
# confirming changes
df['Genre'].dtypes

df.info()
df.nunique()

# Now that our dataset is clean and tidy, we are left with a total of 6 columns and 25551
# rows to dig into during our analysis