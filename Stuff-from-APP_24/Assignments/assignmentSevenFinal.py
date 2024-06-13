import pandas as pd
from matplotlib import pyplot as plt

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))

# Load the Netflix dataset into a pandas DataFrame
df = pd.read_csv("netflix_titles.csv")
df = df.set_index("show_id")

# Data Cleaning and Preparation
# Handled missing data by filling and dropping
df = df.fillna({"director": df["director"].mode()[0], "cast": df["cast"].mode()[0], "country": df["country"].mode()[0]})
# Dropped any other rows with missing data
df = df.dropna()

# Get year from the date_added column and add new column with the data
df["year_added"] = df["date_added"].map(lambda x: x[-4:])
# Changed data type to int64 for easier manipulation
df["year_added"] = pd.to_numeric(df["year_added"])

# A bar graph showing the count of movies vs. TV shows.
def MovieCountVsTvCount():
    # Count the # of content for each type
    data = df.groupby(["type"])["type"].count()
    # Plot the data onto a bar graph
    axes[0,0].bar(data.index, data.values)
    axes[0,0].set_title("# of Movies vs Shows")
    axes[0,0].set_ylabel("Count")

# A line graph depicting the trend of content added over the years.
def ContentAddedPerYear():
    # grouped data by the year added and count the # of values
    data = df.groupby(["year_added"])["year_added"].count()
    # plot the data on a line graph
    axes[0,1].plot(data.index, data.values)
    axes[0,1].set_title("Content added per year")
    axes[0,1].set_xlabel("Year")
    axes[0,1].set_ylabel("Count")

# A histogram of the release years of all titles to show the concentration of old vs new titles.
def OldVsNewYears():
    # plotted histogram by release year
    axes[1,0].hist(df["release_year"])
    axes[1,0].set_xlabel("Year")
    axes[1,0].set_ylabel("Content")
    axes[1,0].set_title("New vs old content")

# A pie chart to represent the proportion of different ratings across all content.
def Ratings():
    # Count number of content ratings
    data = df.groupby(["rating"])["rating"].count()
    # group smaller rating categpries into an other category
    data["Other"] = data[data.values <= 100].values.sum()
    # remove the values added to other category
    data = data[data.values >= 100]
    # plotted pie chart
    axes[1,1].pie(data, labels=data.index, autopct="%1.2f%%")
    axes[1,1].set_title("Proportion of Ratings")

# A scatter plot to explore any relationships between duration and release year (choose appropriate variables like duration for movies and seasons for TV shows).
def DurationMoviesPerYear():
    # Separate the number from the string, and keep the #
    df["duration"] = df["duration"].str.split().str[0]
    # Change the duration to int64
    df["duration"] = pd.to_numeric(df["duration"])
    # Use rows that are type == movie
    movies = df[df["type"] == "Movie"]
    # Plotted scatter plot with the data
    axes[2,0].scatter(movies["release_year"], movies["duration"])
    axes[2,0].set_xlabel("Release Year")
    axes[2,0].set_ylabel("Duration (min)")
    axes[2,0].set_title("Duration of Movies by Year")


# A scatter plot to explore any relationships between duration and release year
def DurationShowsVsYear():
    # Use rows with type == TV show
    shows = df[df["type"] == "TV Show"]
    # Plotted scatter plot with the data
    axes[2,1].scatter(shows["release_year"], shows["duration"])
    axes[2,1].set_xlabel("Release Year")
    axes[2,1].set_ylabel("Duration (seasons)")
    axes[2,1].set_title("Duration of Shows by Year")

# Main function will all graphs
def main():
    MovieCountVsTvCount()
    ContentAddedPerYear()
    OldVsNewYears()
    Ratings()
    DurationMoviesPerYear()
    DurationShowsVsYear()
    plt.show()

# If name of the file is the main call the main function
if __name__ == '__main__':
    main()