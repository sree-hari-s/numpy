# -*- coding: utf-8 -*-
"""Data Structure Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y6aozliJZHllaljggALllA8qxLwX7mDq

1.Create a list named ‘myList’ that is having the following elements: 10,20,30,’apple’, True,8.10.

a. Now in the ‘myList’, append these values: 30,40

b. After that reverse the elements of the ‘myList’ and store that in ‘reversedList’
"""

import numpy as np
myList=np.array([10,20,30,'apple',True,8.10])
myList

myList=np.concatenate((myList,[30,40]))

reversedList=myList[-1::-1]
reversedList

new_rev_list=np.flipud(myList)
new_rev_list

"""2.Create a dictonary with key values as 1,2,3 and the values as ‘data’,’information’, and ‘text’.

a. After that eliminate the ‘text’ value form the dictonary.

b. Add ‘features’ in the dictonary.

c. Fetch the ‘data’ element from the dictonary and display it in the output.
"""

dict1={1:'data',2:'information',3:'text'}
dict1

dict1.pop(3)

dict1

dict1[3]='features'
dict1

dict1[1]

"""3. Create a tuple and add these elements 1,2,3,apple,mango in ‘my_tuple"""

my_tuple=(1,2,3,'apple','mango')
my_tuple

"""4.Create another tuple named numeric_tuple consisting of only integer values 10,20,30,40,50

a. Find the minimum value from the numeric_tuple.

b. Concatenate my_tuple with numeric_tuple and store the result in r1.

c. Duplicate the tuple named my_tuple 2 times and store that in ‘newdupli’.
"""

numeric_tuple=10,20,30,40,50
 numeric_tuple

min(numeric_tuple)

r1=my_tuple+numeric_tuple
r1

r1=np.concatenate((my_tuple,numeric_tuple))
r1

newdupli=my_tuple*2

newdupli

"""5.Create 2 sets with name set1 and set2, where set1 contains{1,2,3,4,5} and set2 to
contains{2,3,7,6,1}

a. Perform the below operation:

a. set1 union set2

b. set1 intersection set2

c. set1 difference set2
"""

set1={1,2,3,4,5} 
set2={2,3,7,6,1}

set1.union(set2)

set1.intersection(set2)

set1.difference(set2)

