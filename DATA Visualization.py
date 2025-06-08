# importing lib.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()


# Data Visualization
# here, we'd use Matplotlib and seaborn for making some informative visuals to gain
# insights abut our data


# setting up seaborn configurations
sns.set_style('whitegrid')

#  Identify top genres and their popularity
# showing stats. on genre column
df['Genre'].describe()


 #visualizing genre column
sns.catplot(y = 'Genre', data = df, kind = 'count',
 order = df['Genre'].value_counts().index,
 color = '#4287f5')
plt.title('genre column distribution')
plt.show()

 #genres which has highest votes and lowest voted

 #visualizing vote_average column
sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
 order = df['Vote_Average'].value_counts().index,
 color = '#4287f5')
plt.title('votes destribution')
plt.show() 

#yearly trens in content addition

df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()




#  What is the most frequent genre in the dataset?
# Drama genre is the most frequent genre in our dataset and has appeared more than
# 14% of the times among 19 other genres.

#  What genres has highest votes ?
# we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the
# highest popularity among fans by being having more than 18.5% of movies popularities.

#  What movie got the highest popularity ? what's its genre ?
# Spider-Man: No Way Home has the highest popularity rate in our dataset and it has
# genres of Action , Adventure and Sience Fiction .

#  What movie got the lowest popularity ? what's its genre ?
# The united states, thread' has the highest lowest rate in our dataset
# and it has genres of music , drama , 'war', 'sci-fi' and history`.

#  Which year has the most filmmed movies?
# year 2020 has the highest filmming rate in our dataset.
