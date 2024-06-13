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

