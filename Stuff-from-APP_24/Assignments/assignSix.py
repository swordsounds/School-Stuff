import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

params = {
        'figure.figsize': (15, 14),
        'toolbar' : 'None'
        }
plt.rcParams.update(params)
fig, axes = plt.subplots(nrows=4, ncols=2)

df = pd.read_csv('videogames.csv')
# o Check for any missing values in the 'Year' and 'Global_Sales' columns and handle them
print(df.isnull().sum())
# by filling missing years with the median year and sales with the mean sales value.
df = df.fillna({'Year': df['Year'].median(), 'Global_Sales': df['Global_Sales'].mean()})
df = df.drop_duplicates()
df['Year'] = df['Year'].map(lambda x: float(x))


# Yearly Game Releases: Calculate and visualize the total number of games released each year using a line graph.
def TotalGamesPerYear():
    data = df.groupby(['Year'])['Name'].agg('count')
    axes[0,0].plot(data, marker='o')
    axes[0,0].set_xlabel('Years')
    axes[0,0].set_ylabel('Games Released')
    axes[0,0].set_title('Games Released Per Year')

# Platform Popularity: Identify the platform with the highest number of releases and visualize all platforms' releases using a bar chart.
def HighestReleasesPerPlatform():
    data = df.groupby(['Platform'])['Name'].agg({'count'})
    axes[1,0].bar(data.index, data['count'], color=('grey', 'blue', 'red', 'green'))
    axes[1,0].set_xlabel('Platforms')
    axes[1,0].set_ylabel('Total Releases')
    axes[1,0].set_title('Total Releases Per Platform')
    axes[1,0].set_xticklabels(axes[1,0].get_xticklabels(), rotation=45)

# Top Selling Games: List the top 5 best-selling games of all time in a formatted table.
def TopFiveBestSelling(df):
    df = df.sort_values(by=['Global_Sales'], ascending=False).head()
    table = axes[2,0].table(cellText=df.values, colLabels=df.columns, loc='center')
    table.scale(1, 2)
    axes[2,0].set_axis_off()

# Genre Popularity: Create a pie chart to show the market share of each game genre based on global sales.
def GenrePopularity():
    data = df.groupby(['Genre'])['Global_Sales'].agg({'sum'})
    axes[0,1].pie(data['sum'], labels=data.index, autopct='%1.1f%%')
    axes[0,1].set_title('Genre Popularity')

# o Sales vs. Year Scatter Plot: Generate a scatter plot to explore the relationship between the year of release and global sales, including a trend line.
def SalesVsYear():
    data = df.groupby(['Year'])['Global_Sales'].agg({'sum'})
    axes[1,1].plot(data.index, data['sum'], marker='o')
    axes[1,1].set_xlabel('Years')
    axes[1,1].set_ylabel('Total Sales')
    axes[1,1].set_title('Total Sales Per Year')


# Sales Distribution by Platform: Use box plots to compare the global sales figures across different platforms, highlighting any outliers.
def SalesPerPlatform():
    df.boxplot(column='Global_Sales', by='Platform', ax=axes[2,1])
    axes[2,1].set_xlabel('Platforms')
    axes[2,1].set_ylabel('Total Sales')
    axes[2,1].set_title('Total Sales Per Platform')
    axes[2,1].set_xticklabels(axes[2,1].get_xticklabels(), rotation=45)

# o Annual Sales Trends: Compute and plot the total global sales per year to see how video game sales have evolved.
def AnnualSalesTrend():
    data = df.groupby(['Year'])['Global_Sales'].agg({'sum'})
    axes[3,0].scatter(data.index, data['sum'])
    axes[3,0].set_title('Annual Sales')
    axes[3,0].set_xlabel('Years')
    axes[3,0].set_ylabel('Global Sales (millions)')
    axes[3,1].set_visible(False)

    line = np.polyfit(data.index, data['sum'], 1)
    line1 = np.poly1d(line)
    axes[3,0].plot(data.index, line1(data.index),'r--')

TotalGamesPerYear()
HighestReleasesPerPlatform()
TopFiveBestSelling(df)
GenrePopularity()
SalesVsYear()
SalesPerPlatform()
AnnualSalesTrend()

plt.subplots_adjust(left=0.06,
                    bottom= 0.06,
                    right=0.99,
                    top=0.9,
                    wspace=0.12,
                    hspace=0.99)
plt.suptitle("Graphs")
plt.show()

#  For each plot, include a title, labels for x and y axes, and a legend if applicable.