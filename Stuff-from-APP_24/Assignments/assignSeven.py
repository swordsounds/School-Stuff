import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))


# Load the Netflix dataset into a pandas DataFrame.
df = pd.read_csv('netflix_titles.csv')
df.set_index('show_id')

# Data Cleaning and Preparation
# Handle missing data by filling or dropping (instruct students on preferred method).

df = df.fillna({'director': df['director'].mode()[0], 'cast': df['cast'].mode()[0], 'country': df['country'].mode()[0], 'date_added': df['date_added'].mode()[0]})
df = df.dropna()

# Get just the year from the date_added column and add a new column with the data
df["year_added"] = df["date_added"].map(lambda x: x[-4:])

# Change the data type to int64
df["year_added"] = pd.to_numeric(df["year_added"])
# Number of Movies vs. Shows

# A bar graph showing the count of movies vs. TV shows.
def MovieCountVsTvCount():
    data = df.groupby(['type'])['title'].agg('count')
    axes[0,0].bar(data.index, data.values)
    axes[0,0].set_xlabel('Type')
    axes[0,0].set_ylabel('Count')
    axes[0,0].set_title('Movie Count vs. TV Show Count')
 

# A line graph depicting the trend of content added over the years.
def ContentAddedPerYear():
    df['release_year'] = df['date_added'].map(lambda x: x[-4:])
    data = df.groupby(['release_year'])['title'].agg('count')
    axes[0,1].plot(data.index, data.values)
    axes[0,1].set_xlabel('Year')
    axes[0,1].set_ylabel('Count')
    axes[0,1].set_title('Content Added Per Year')
    

# A histogram of the release years of all titles to show the concentration of old vs.new titles.
def OldVsNewYears():
    axes[1,0].hist(df['release_year'])
    axes[1,0].set_xlabel('Year')
    axes[1,0].set_ylabel('Count')
    axes[1,0].set_title('New vs. Old')


# A pie chart to represent the proportion of different ratings across all content.
def Ratings():
    # Count number of content ratings
    data = df.groupby(["rating"])["rating"].count()
    # group smaller rating categpries into an other category
    data["Other"] = data[data.values <= 300].values.sum()
    # remove the values added to other category
    data = data[data.values >= 300]
    # plot a pie chart
    axes[1,1].pie(data, labels=data.index, autopct="%1.2f%%")
    axes[1,1].set_title('Ratings')

# A scatter plot to explore any relationships between duration and release year (choose appropriate variables like duration for movies and seasons for TV shows).
def DurationVsYear():

    df["duration"] = df["duration"].str.split().str[0]
    # Change the duration to int64
    df["duration"] = pd.to_numeric(df["duration"])

    movies = df[df['type'] == 'Movie']
    axes[2,0].scatter(movies['release_year'], movies['duration'])

    shows = df[df["type"] == "TV Show"]
    # Plot a scatter plot with the data
    axes[2, 1].scatter(shows["release_year"], shows["duration"])

# # Separate the number from the unit ([60, "minutes"]) and keep the first value (the number)
# df["duration"] = df["duration"].str.split().str[0]
# # Change the duration to int64
# df["duration"] = pd.to_numeric(df["duration"])
# # Take all rows that are type = movie
# df_movies = df[df["type"] == "Movie"]
# # Plot a scatter plot with the data
# plt.scatter(df_movies["release_year"], df_movies["duration"])
# plt.xlabel("Release Year")
# plt.ylabel("Duration (min)")
# plt.title("Duration of movies by year")
# plt.show()

# # Take all rows with type = TV show
# df_shows = df[df["type"] == "TV Show"]
# # Plot a scatter plot with the data
# plt.scatter(df_shows["release_year"], df_shows["duration"])
# plt.xlabel("Release Year")
# plt.ylabel("Duration (seasons)")
# plt.title("Duration of shows by year")
# plt.show()
 
# Submission:
MovieCountVsTvCount()
ContentAddedPerYear()
OldVsNewYears()
Ratings()
DurationVsYear()

plt.show()
