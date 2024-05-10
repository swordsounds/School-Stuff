import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Tasks:

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 14))
df = pd.read_csv('videogames.csv')
# o Check for any missing values in the 'Year' and 'Global_Sales' columns and handle them
print(df.isnull().sum())
# by filling missing years with the median year and sales with the mean sales value.
df = df.fillna({'Year': df['Year'].median(), 'Global_Sales': df['Global_Sales'].mean()})
df = df.drop_duplicates()
df['Year'] = df['Year'].map(lambda x: float(x))


# Yearly Game Releases: Calculate and visualize the total number of games released each year using a line graph.
def TotalReleasePerYear():
    x = []
    y = []
    for i in range(2000, 2024):
        y.append(sum((df.loc[df['Year'] == float(i)])['Global_Sales']))
        x.append(i)
    axes[0,0].plot(x, y)
    axes[0,0].set_xlabel('Years')
    axes[0,0].set_ylabel('Total Releases')
    axes[0,0].set_title('Total Releases Per Year')

# Platform Popularity: Identify the platform with the highest number of releases and visualize all platforms' releases using a bar chart.
def HighestReleasesPerPlatform():
    x = []
    y = []
    for i in df['Platform'].unique():
        y.append(sum((df.loc[df['Platform'] == i])['Global_Sales']))
        x.append(i)
    axes[1,0].bar(x, y)
    axes[1,0].set_xlabel('Platforms')
    axes[1,0].set_ylabel('Total Releases')
    axes[1,0].set_title('Total Releases Per Platform')
    axes[1,0].set_xticklabels(axes[1,0].get_xticklabels(), rotation=45)

# Top Selling Games: List the top 5 best-selling games of all time in a formatted table.
def TopFiveBestSelling(df):
    df = df.sort_values(by=['Global_Sales'], ascending=False).head()
    axes[2, 0].table(cellText=df.values, colLabels=df.columns, loc='center')

# Genre Popularity: Create a pie chart to show the market share of each game genre based on global sales.
def GenrePopularity():
    x = []
    y = []
    for i in df['Genre'].unique():
        y.append(sum((df.loc[df['Genre'] == i])['Global_Sales']))
        x.append(i)
    axes[0,1].pie(y, labels=x)
    axes[0,1].set_title('Genre Popularity')

# o Sales vs. Year Scatter Plot: Generate a scatter plot to explore the relationship between the year of release and global sales, including a trend line.
def SalesVsYear():
    x = []
    y = []
    for i in range(2000, 2024):
        y.append(sum((df.loc[df['Year'] == float(i)])['Global_Sales']))
        x.append(i)
    axes[1,1].scatter(x, y)
    axes[1,1].set_xlabel('Years')
    axes[1,1].set_ylabel('Total Sales')
    axes[1,1].set_title('Total Sales Per Year')


# Sales Distribution by Platform: Use box plots to compare the global sales figures across different platforms, highlighting any outliers.
def SalesPerPlatform():
    x = []
    y = []
    for i in df['Platform'].unique():
        y.append(sum((df.loc[df['Platform'] == i])['Global_Sales']))
        x.append(i)
    axes[2,1].scatter(x, y)
    axes[2,1].set_xlabel('Platforms')
    axes[2,1].set_ylabel('Total Sales')
    axes[2,1].set_title('Total Sales Per Platform')
    axes[2,1].set_xticklabels(axes[2,1].get_xticklabels(), rotation=45)

TotalReleasePerYear()
HighestReleasesPerPlatform()
TopFiveBestSelling(df)
GenrePopularity()
SalesVsYear()
SalesPerPlatform()
plt.show()




# o Annual Sales Trends: Compute and plot the total global sales per year to see how video game sales have evolved.

# Visualizations: Appropriately labeled plots with interpretations for each visualization included in the analysis.

#  For each plot, include a title, labels for x and y axes, and a legend if applicable.
