import numpy as np
#A1 You have the following list:
# my_list = [2,4,-4,8,1,7,-5]
# Make the list into an array called my_array.

my_list = [2,4,-4,8,1,7,-5]

my_array = np.array(my_list)
print(my_array)

#A2
#It has one dimension

#A3
#It has 1 row and 7 columns

#A4 Make an array with 7 rows and 1 column, 
# containing only the number zero.
a4_array = np.zeros((7,1))
print(a4_array)

#A5. Make an array which returns True if the 
# corresponding element in my_array is larger or 
# equal to the corresponding elements in the array 
# made in A4 and False otherwise.

a5_array = np.greater_equal(my_array, a4_array)
print(a5_array)

#A6. Make an array with numbers from -2 to 2 
# with 17 equally spaced elements, i.e. 
# the start of the elements are -2, -1.75, -1.5, … etc.

a6_array = np.linspace(-2, 2, 17)
print(a6_array)
