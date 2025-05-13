# importing lib.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mymoviedb.csv')
df.head()

# viewing dataset info
df.info()

# exploring genres column
df['Genre'].head()


# check for duplicated rows
df.duplicated().sum()
0
# our dataset has no duplicated rows either.
# exploring summary statistics
df.describe()

# • Exploration Summary
# • we have a dataframe consisting of 9827 rows and 9 columns.
# • our dataset looks a bit tidy with no NaNs nor duplicated values.
# • Release_Date column needs to be casted into date time and to extract only the year
# • Overview, Original_Languege and Poster-Url wouldn't be so useful during analysis
# • there is noticable outliers in Popularity column
# • Vote_Average bettter be categorised for proper analysis.
# • Genre column has comman saperated values and white spaces that needs to be handle


