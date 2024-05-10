import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Tasks:

df = pd.read_csv('videogames.csv')
# o Check for any missing values in the 'Year' and 'Global_Sales' columns and handle them
print(df.isnull().sum())
# by filling missing years with the median year and sales with the mean sales value.
df['Year'] = df['Year'].fillna(np.median(df['Year']))
df['Global_Sales'] = df['Global_Sales'].fillna(np.mean(df['Global_Sales']))
df = df.drop_duplicates()
print(df)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 14))

axes[0, 1].plot(df['Year'].sort_values(ascending=False), df['Global_Sales'])
plt.show()

#  Exploratory Data Analysis:
# o Yearly Game Releases: Calculate and visualize the total number of games released each
# year using a line graph.
# o Platform Popularity: Identify the platform with the highest number of releases and
# visualize all platforms' releases using a bar chart.
# o Top Selling Games: List the top 5 best-selling games of all time in a formatted table.
#  Sales Trends Analysis:
# o Annual Sales Trends: Compute and plot the total global sales per year to see how video
# game sales have evolved.
# o Genre Popularity: Create a pie chart to show the market share of each game genre
# based on global sales.


#  Advanced Visualization:
# o Sales vs. Year Scatter Plot: Generate a scatter plot to explore the relationship between
# the year of release and global sales, including a trend line.
# o Sales Distribution by Platform: Use box plots to compare the global sales figures across
# different platforms, highlighting any outliers.

# Deliverables:
# Code: A .py file containing your code
# Visualizations: Appropriately labeled plots with interpretations for each visualization included in the
# analysis.
# Guidance for Students:
#  Include comments in your code to explain the purpose of each Python statement.
#  For each plot, include a title, labels for x and y axes, and a legend if applicable.
