import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))
# Load the Netflix dataset into a pandas DataFrame.
df = pd.read_csv('netflix_titles.csv')
# df.set_index('show_id')
# Data Cleaning and Preparation
# Handle missing data by filling or dropping (instruct students on preferred method).

print(df.isna().sum())
df = df.fillna({'director': df['director'].mode()[0], 'cast': df['cast'].mode()[0], 'country': df['country'].mode()[0], 'date_added': df['date_added'].mode()[0]})
df = df.dropna()

# o Convert columns to appropriate data types, if necessary.
# o Analyze the distribution of movies vs. TV shows.
# o Investigate the number of titles added each year.
# o Explore the ratings (like TV-MA, TV-14) distribution for different types of content.


# A bar graph showing the count of movies vs. TV shows.

def MovieCountVsTvCount():
    data = df.groupby(['type'])['title'].agg('count')
    axes[0,0].bar(data.index, data)
    axes[0,0].set_xlabel('Type')
    axes[0,0].set_ylabel('Count')
    axes[0,0].set_title('Movie Count vs. TV Show Count')
 

# A line graph depicting the trend of content added over the years.
def ContentAddedPerYear():
    df['release_year'] = df['date_added'].map(lambda x: x[-4:])
    data = df.groupby(['release_year'])['title'].agg('count')
    axes[0,1].plot(data.index, data)
    axes[0,1].set_xlabel('Year')
    axes[0,1].set_ylabel('Count')
    axes[0,1].set_title('Content Added Per Year')
    

# A histogram of the release years of all titles to show the concentration of old vs.new titles.
def OldVsNewYears():
    axes[1,0].hist(df['release_year'])
    axes[1,0].set_xlabel('Year')
    axes[1,0].set_ylabel('Count')
    axes[1,0].set_title('Old vs. New Years')


# A pie chart to represent the proportion of different ratings across all content.
def Ratings():
    data = df.groupby(['rating'])['title'].agg('count')
    axes[1,1].pie(data, labels=data.index, autopct='%1.1f%%')
    axes[1,1].set_title('Ratings')

# A scatter plot to explore any relationships between duration and release year (choose appropriate variables like duration for movies and seasons for TV shows).
def DurationVsYear():
    movies = df[df['type'] == 'Movie']
    axes[2,0].scatter(movies['release_year'].sort_values(ascending=False), movies['duration'].map(lambda x: x.split(' ')[0]))

    shows = df[df['type'] == 'TV Show']
    axes[2,1].scatter(shows['release_year'].sort_values(ascending=False), shows['duration'].map(lambda x: x.split(' ')[0]).sort_values(ascending=True))


 
# Submission:
MovieCountVsTvCount()
ContentAddedPerYear()
OldVsNewYears()
Ratings()
DurationVsYear()

plt.show()

# Submit code and 5 graphs to the appropriate dropbox