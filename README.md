
# Netflix Movie Analysis
![Netflix_Logo_RGB](https://github.com/user-attachments/assets/8af6d32b-7027-44a6-ba0b-38021fb8468b)

# Project Overview

• Netflix is a global streaming platform offering a wide range of content

• This project explores Netflix's content to 
uncover patterns and insights.


• Focus is on understanding what type of 
content is most common and popularA brief description of what this project does and who it's for.

## Objective


```bash
  1.Most frequent gener of movies
  
  2.Identify the genres of higest popular movies.

  3.Identify the genre of lowest popular movies.

  4.Discover yearly trends in content addition.

```

## Project Framework

Dataset from Kaggle: Netflix movie 

Tools : Python(Pandas, Numpy, Matplotlib, Seaborn)
Jupyter Notebook


| Steps             | Tools                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Data preprocessing | Pandas
| Exploratory Data Analysis | Pandas + Numpy  |
| Data vistualization | Seaborn + Matplotlib |
| Insight Genration | Pandas + Numpy + Seaborn + Matplotlib|

## Steps:
1.Dataset overview

2.Data preprocessing

3.Exploratory Data Analysis

4.Data vistualization

5.Insight Genration


## Dataset overview

![1](https://github.com/user-attachments/assets/b1dd6309-709f-4945-b920-3e62788b4163)

![2](https://github.com/user-attachments/assets/9611405f-3f6c-41f6-966f-f5511e029eb2)

![3](https://github.com/user-attachments/assets/70d4e910-4aba-4931-8137-5df14239300b)

![4](https://github.com/user-attachments/assets/8edb21e7-a7d6-4f05-8014-6852f9ef0992)

• looks like our dataset has no NaNs! • Overview, Original_Language and Poster-Url
wouldn't be so useful during analysis • Release_Date column needs to be casted into
date time and to extract only the year value

## Data preprocessing

1.Data Transformation

By changing the Release Date data type form object into Integer

![5](https://github.com/user-attachments/assets/22a5b915-0931-438f-997f-1502fd37d357)



2.Data cleaning

 Overview, Original_Languege and Poster-Url wouldn't be so useful during Analysis
 
![6](https://github.com/user-attachments/assets/30cf4621-500f-44e8-a257-3b1f781f93c3)




 ## Exploratory Data Analysis

 1.Categorizing Vote_Average column
We would cut the Vote_Average values and make 4 categories: popular average
below_avg not_popular to describe it more using catigorize_col() 

![7](https://github.com/user-attachments/assets/5d80b529-9d55-4d80-8cb2-acc66b001fa9)


2.we'd split genres into a list and then
explode our dataframe to have only one
genre per row for each movie

![8](https://github.com/user-attachments/assets/c0286bd8-a50a-4967-9968-4016a18dfa6c)

Now that our dataset is clean and tidy, we are left with a total of 6 columns and 25551
rows to dig into during our analysis

![9](https://github.com/user-attachments/assets/4a0b8cb2-4269-4a6b-a69d-6e57b5ddceaf)






























 















