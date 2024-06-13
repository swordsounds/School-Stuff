import pandas as pd

df1 = pd.DataFrame(
    {'a' : [1, 2, 3],
     'b': [1, 2, 3],
     'c' : [1, 2, 3]}
)

df2 = pd.DataFrame(
    [[4, 7, 10],
    [5, 8, 11],
    [6, 9, 12]],
    index=[1, 2, 3],
    columns=['a', 'b', 'c'])

df3 = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = pd.MultiIndex.from_tuples(
    [('d', 1), ('d', 2),
    ('e', 2)], names=['n', 'v']))


# There are many ways to add a row to a data frame. This section will cover two of them – the append() function and add Series as a row in the dataframe

# Example 1: Add a row to the dataframe using the append() function

# List of Tuples
students = [ ('jack', 24, 'Ottawa' , 'Canada') ,
		('Riti', 20, 'Delhi' , 'India' ) ,
		('Vikas', 31, 'Halifax' , 'Canada' ) ,
		('Neelu', 32, 'Cupids' , 'Canada' ) ,
		('John', 26, 'New Perlican' , 'Canada') ,
		('Mike', 19, 'Goulds' , 'Canada')  ]

#Create a DataFrame object
df = pd.DataFrame(  students, 
		columns = ['Name' , 'Age', 'City' , 'Country'],
		index=['a', 'b', 'c' , 'd' , 'e' , 'f']) 


# Pass the row elements as key value pairs to append() function 
mod_df = df._append({'Name' : 'Sahil', 'Age' : 22} , ignore_index=True)  # notice no values for city or country


raw_data = {'name': ['Homer Simpson', 'Al Greener', 'Muffin Man', 'Spencer Davis'],
	'age': [20, 19, 22, 21],
	'favorite_color': ['blue', 'red', 'yellow', "green"],
	'grade': [88, 92, 95, 70]}

df = pd.DataFrame(raw_data, index = ['Homer Simpson', 'Al Greener', 'Muffin Man', 'Spencer Davis'])

df.to_csv('myDataFrame.csv')  # a comma seperated csv file will be created

print(df1)
print()
print(df2)
print()
print(df3)
print()
print('\nOriginal Dataframe')
print(df)
print()
print('\nModified Dataframe')
print(mod_df)

# DataFrame functions
# df.head( )	By default, returns the first 5 rows of the DataFrame. To change the default, you may insert an argument between the parenthesis to change the number of rows returned.
# df.tail( )	By default, returns the last 5 rows of the DataFrame. This function is used to get the last n rows. This function returns the last n rows from the object based on position.
# df.info( )	Helps in getting a quick overview of the dataset. This function is used to get a brief summary of the DataFrame. This method prints information about a DataFrame including the index dtype and column dtypes, non-null values, and memory usage.
# df.shape	Returns an int representing the number of elements in this object. Return the number of rows if Series, otherwise returns the number of rows times the number of columns if DataFrame.
# df.size	
# Returns an int representing the number of elements in this object. Return the number of rows if Series. Otherwise return the number of rows times number of columns if DataFrame.

# df.ndim	Returns dimension of DataFrame/Series. 1 for one dimension (Series), 2 for two dimensions (DataFrame).
# df.describe( )	Return a statistical summary for numerical columns present in the dataset. This method calculates some statistical measures like percentile, mean and standard deviation of the numerical values of the Series or DataFrame.
# df.sample( )	Used to generate a sample randomly either row or column. It allows you to select values randomly from a Series or DataFrame. It is useful when we want to select a random sample from a distribution.
# df.isnull( ).sum( )	Returns the number of missing values in each column.
# df.nunique( )	Returns number of unique elements in the object. It counts the number of unique entries over columns or rows. It is very useful in categorical features especially in cases where we do not know the number of categories beforehand
# df.index	Searches for a given element from the start of the list and returns the lowest index where the element appears.
# df.columns	Returns the column labels of the DataFrame
# df.memory_usage( )	Returns how much memory each column uses in bytes. It is useful especially when we work with large data frames
# df.dropna( )	Used to remove a row or a column from a DataFramethat has a NaN or missing values in it
# df.nlargest( )	Returns the first n rows ordered by columns in descending order.
# df.isna( )	Returns a DataFrame filled with boolean values with true indicating missing values
# df.duplicated( )	Returns a boolean Series denoting duplicate rows
# df.value_counts( )	Used to get a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently occurring element. It excludes missing values by default. This function comes in handy when we want to check the problem of class imbalance for a categorical variable.
# df.corr( )	Used to find the pairwise correlation of all columns in the DataFrame. Any missing values are automatically excluded. For any non-numeric data type columns in the DataFrame, it is ignored. This function comes in handy while we doing the Feature Selection by observing the correlation between features and target variable or between variables.
# df.dtypes	Shows the data type of each column.