import numpy as np
array1 = np.random.randint(0,100,size=(4,10))
print (array1)


# Output:

# [[68 56 72 91 64 98  3 54 49 67]
# [ 1  6 54 65 24 97 68  9 28 47]
# [30 88 52 11 22 12 35 65 66  3]
# [13 83 81 32 87 74 79 34 26  1]]

#ceate a mask showing numbers greater than 70.

mask = array1 > 70

print(mask)


# Output

# [[False False  True  True False  True False False False False]
# [False False False False False  True False False False False]
# [False  True False False False False False False False False]
# [False  True  True False  True  True  True False False False]]

#Use the mask to extract the numbers:

print (array1[mask])


# Output
# [72 91 98 97 88 83 81 87 74 79]

			
# Using any and all
# NumPy any() function is used to check whether an array element along the mentioned axis evaluates to True or False. If there is an element in a particular axis that is True, it returns True

# Numpy all() function returns True only if all elements in a NumPy array evaluate to True


print (mask.any())
print (mask.all())


# Output
# True
# False

			

# It can also be applied column-wise (by passing axis=1) or row-wise (by passing axis=1).


print ('All tests in a column are true:')
print (mask.all(axis=0))
print ('\nAny test in a row is true:')
print (mask.any(axis=1))


# Outout:

# All tests in a column are true:
# [False False False False False False False False False False]

# Any test in a row is true:
# [False  True  True  True]

			
# Selecting rows or columns based on one value in that row or column

#Select all columns where the value of the first element is equal to, or greater than 70:

mask = array1[0,:] >= 70 # colon indicates all columns, zero indicates row 0
print ('\nShowing the mask')
print (mask)
print ('\nThe mask applied to all columns')
print (array1[:,mask]) # colon represents all rows of chosen columns


# Output

# Showing the mask
# [False False False False False False  True False False False]

# The mask applied to all columns
# [[98]
# [78]
# [77]
# [ 5]]

import numpy as np
import pandas as pd


s1 = pd.Series([11, 28, 72, 3, 5, 8])
print ("S is:\n",s1)

# You can directly access the index and the values in a Series


print(s1.index)
print(s1.values)


# Output
# RangeIndex(start=0, stop=6, step=1)
# [11 28 72  3  5  8]


import numpy as np
import pandas as pd

sport = ['ultimate', 'basketball', 'baseball', 'soccer']
players = [20, 32, 22, 26]
s1 = pd.Series(players, index= sport) 
print ("\nSport and number of players: \n", s1)


# Output
# Sport and number of players: 
# ultimate      20
# basketball    32
# baseball      22
# soccer        26
# dtype: int6

import numpy as np
import pandas as pd

sport = ['ultimate', 'basketball', 'baseball', 'soccer']
playersHS = [20, 32, 22, 26]
playersJH = [33, 45, 25, 35]
s1 = pd.Series(playersHS, index= sport)
s2 = pd.Series(playersJH, index= sport)
print ("\nSport and number of players: \n", s1 + s2)
print("Sum of players in High School: ", sum(s1))
print("Sum of players in Junior High: ", sum(s2))


# Output
# Sport and number of players: 
# ultimate      53
# basketball    77
# baseball      47
# soccer        61
# dtype: int64
# Sum of players in High School:  100
# Sum of players in Junior High:  138