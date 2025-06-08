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





