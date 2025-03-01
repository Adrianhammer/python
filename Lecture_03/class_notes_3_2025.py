# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:29:14 2025

@author: basiv7626
"""

#Sequential

x= 10
y=5
z= x+y
print(z)

#Selection Control

user_input= int(input("Enter odd or even number? "))

if user_input % 2==0:
    print("even")
else:
    print("odd")


#Iterative Control

""" Print numbers from 0 till a user specifed vale"""

user_specified_value= int(input("Please enter a value to print till?"))

current=1

while current <=user_specified_value:
    print(current)
    current=current+1


"""Sum a sequence of numbers"""


user_specified_value= int(input("Please enter a value to print till?"))

current=1
sum_1=0

while current <=3:
    sum_1= sum_1 +current
    #print(current)
    current=current+1

print(f"the sum is {sum_1}")


#%%

"""While loop functions only the condition is true"""

current=5

while current <=3:  #since 5 is not less than 3
    print(current)
    current=current+1

#There are 3 types of while loops

"""Infinite Loops"""

current= 1
while current <=3:  #since 5 is not less than 3
    print(current)
    #current= current+1
    
"""Definite Loop- You know the number of times a loop will iterate in the start"""

current= 1
while current <=5:  #since 5
    print(current)
    current= current+1
    
"""Indefinite Loop-  You do not know the number of times a 
loop will iterate in the start """

"""it is used to check the user-supplied values"""

choice = input("Enter A or B:")

while choice not in ("A", "B"):
    print("Wrong choice")
    choice= input("Enter A or B")


print(f"Your choice was {choice}")
    
#%%

"""
P4. Write a program that sums a
series of (positive) integers entered by
the user, excluding all numbers
that are greater than 100.
"""
# Ask the user for input
num = int(input('Enter first number to sum (enter -1 to exit): '))
# Initialize total
total = 0
# While not quit
while num != -1:
    if (num >= 0) and (num <= 100):
        total = total + num
    num = int(input('Enter next number: '))
# display sum
print(f'sum = {total:.0f}')


""" Lists, Tuples and String"""

"""Lists"""

fruits= ["apple", "orange", "banana"]
type(fruits)
len(fruits)
print(fruits)


"""Selecting data within a list"""

fruits[1]

mixed_lists= ["apple", 2,True, 4, "Orange"]

mixed_lists[1] + mixed_lists[3]


#Common list operations

list1= [3,2,1,4]

list1.sort()
print(list1)

list1[3]= "four"
list1


del list1[0]
list1

#append

list1.append("Five")
list1

list2= [2,3,4,5]

list2.reverse()
list2

sum(list2)

list3= ["one", "two", "three"]
x, y, z= list3
print(x, y, z)

#Nested lists

integers= [[1,2,3], [99, 98, 97]]

print(integers)

"""Lists are MUTABLE- You can modify things with a list """


"""TUPLES"""

fruits= ("apple", "fruits")
type(fruits)
len(fruits)
print(fruits)


fruits[1]

fruits[0]= "Orange"


tuple_with_one= ("Five" , )
type(tuple_with_one)

tuple_with= ("Five"  )
type(tuple_with)



#String slicing

string1= "hello"

string1[1:]

list1= [3,2,1,4]

list1[1:]

list1[2:]


#%%

"""
P1. Write a Python program that prompts the user 
for a list of integers,
stores in another list only those values 
between 1–100 and displays the
resulting list.
"""

x= int(input("Please give a number to store in a list the code will break if you enter -1"))

list_1=[]

while x !=-1:
    if x >0 and x<100:
        list_1.append(x)
    x= int(input("Please give a number to store in a list the code will break if you enter -1"))
print(f"These are the numbers entered: {list_1} ")
        
#%%
tuple_1= (2, 3, 4, 9)
print(f"The valid numbers are {tuple_1}")

x = int(input("Please give a valid number to store in a "
              "list. The code will break if you enter -1: "))
list1_1 =[]


while x!=-1:
    if x in tuple_1:
        list1_1.append(x)
    else:
        print("Invalid Value")
    x= int(input("Enter a valid value "))

print(list1_1)



#%%

"""
P3. Write a Python program that prompts the user for a list of integers
and stores them in a list. For all values that are greater than 100, the
string 'over' should be stored instead. The program should display the
resulting list.
"""



x= int(input("Please give a number to store in a list"
             "the code will break if you enter? "))

list_1=[]

while x !=-1:
    if x >100:
        list_1.append("over")
    else:
        list_1.append(x)
    x= int(input("Please give a number to store in a list the code will break if you enter -1"))



print(f"These are the numbers entered: {list_1} ")
        

#%%

x= (input("Please give a string to store in a list"
             "the code will break if you enter? "))

list_1=[]

while x !="":
    list_1.append(x)
    
    x= (input("Please give a string to store in a list the code will break if you enter -1"))

print(list_1)























\






























