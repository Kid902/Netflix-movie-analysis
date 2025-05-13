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


