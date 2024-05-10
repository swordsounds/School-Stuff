import pandas as pd
import numpy as np




def main():
    df = pd.read_csv('resort.csv')

    #Part 1: Explore the data by viewing the top and bottom entries and get a random sample of the data to see a variety of entries.

    print('Head:\n',df.head(),'\n--------------------------------\n')
    print('Tail:\n',df.tail(),'\n--------------------------------\n')
    print('Sample:\n',df.sample(n=1),'\n--------------------------------\n')

    #Part 2: Check for any duplicate records in the data. Discuss why it might be important to remove duplicates.

    print('Sum of Null Values:\n',df.isnull().sum(),'\n--------------------------------\n')
    print('Sum of Duplicates:\n',df.duplicated(),'\n--------------------------------\n')
    df = df.fillna(np.mean(df['RunTime'])).drop_duplicates()


    #Part 3: Calculate some basic statistics for the numerical columns like RunTime to understand things like average performance times.
    Difficulty_Index = {
        'Beginner' : 10,
        'Intermediate' : 20,
        'Advanced' : 30,
        'Expert' : 40
    }
    print('Average RunTime:\n',df['RunTime'].mean(),'\n--------------------------------\n')
    #Look at how different variables like RunTime and SlopeDifficulty might relate to each other by checking if there's any pattern or relationship between them.
    print('Relation of RunTime and SlopeDiff:\n',df['RunTime'].corr(df['SlopeDifficulty'].map(Difficulty_Index), method='pearson'),'\n--------------------------------\n')
    #Investigate how many unique values are in the WeatherConditions to understand the variety of weather conditions recorded.
    print('Weather Types:\n',df['WeatherConditions'].unique(),'\n--------------------------------\n')
    #Get summary statistics with describe and explore relationships with corr.
    print('Summary of stats:\n',df.describe(),'\n--------------------------------\n')
    print('Correlation of RunTime w/ SlopeDiff:\n',df['RunTime'].corr(df['SlopeDifficulty'].map(Difficulty_Index), method='pearson'),'\n--------------------------------\n')


    #Part 4: Add a new column that might help in understanding the data better, such as a performance score derived from RunTime and SlopeDifficulty.
    df['PerformanceScore'] = df['RunTime'] * df['SlopeDifficulty'].map(Difficulty_Index)
    df = df.assign(PerformanceScore=df['PerformanceScore'])
    #Sort the data by interesting features like the fastest run times or the hardest slopes.

    print('Grouped data by RunTime:\n',df.groupby('SkierName')['RunTime'].mean().sort_values(ascending=True),'\n--------------------------------\n')


    #Group the data by categories such as Date or WeatherConditions to explore how certain conditions affect the skiers' performances.

    print('Grouped data by Date:\n',df.groupby('Date')['PerformanceScore'].mean().sort_values(ascending=False),'\n--------------------------------\n')

if __name__ == '__main__':
    main()