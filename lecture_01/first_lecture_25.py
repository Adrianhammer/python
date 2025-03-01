# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:14:27 2025

@author: basiv7626
"""

first_code= "Hello Python"
print(first_code)


"""Variables"""

tom_hanks = 60
print(tom_hanks)

#Update your variables

tom_hanks = tom_hanks + 10
print(tom_hanks)

#Smae value can be given to different variables

matt_damon= 60
print(matt_damon)

#Another example

k= 30
print(k)
j=30
print(j)


type(k)

num_eg= 22.345
type(num_eg)



hello= "Welcome to Python"
print(hello)
type(hello)

"""Variable Naming Rules"""
#You cannot start a variable name with a number
6pack= 12

#This is legal
pack6 = 66


six pack= 66

six_pack = 66
print(six_pack)


"""Its illegal to have some special characters in your variable names"""

jack!= 22

'name1'= 22



#%%

"""Numeric data"""

x= 1024
print(x)

y= 1023.5655
print(y)

z= 1023,233  ##Incorrect code
print(z)


i= 787777777777777777777777777777777700000000000000000765
print(i)


j=  78777777777777777777777777777.7777700000000000000000765
print(j)

small_number= 0.00044444444444999999999999999999999

print(small_number)


"""String"""

string1= "Hello"
len(string1)

print("There are my favourite number: \n1, \n35, \n44")


"""INPUT FUNCTION"""

input("Enter your favorite color?")


fruits= input("What fruit did you buy?")
print(fruits)

fruit_killo= int(input("How many killos of fruit did you buy?"))
print(fruit_killo)

type(fruit_killo)

discount_offer= fruit_killo+0.5
discount_offer



value_purchased= float(input("What is the value of items you shopped?"))
print(value_purchased)
type(value_purchased)



string1="Hello" 
print(string1*5)

#%%
#Output Formattings

color1= "Red"
color2="Yellow"
print(f"My favourite colors are {color1} and {color2}")

print(f"My favourite colors are {color1.upper()} and {color2.upper()}")



price_bottle = 2199.57                  # price per bottle
litre_sold = 18.23                    
total_revenue = price_bottle*litre_sold 

total_revenue

print(f"the total revenue is {total_revenue: .4f}")


print(f"the total revenue is {total_revenue: .2e}")


print(f"the total revenue is {total_revenue: ,}")


#%%



num1= int(input("Enter the first number you want to divide?"))
num2= int(input("Enter the second number you want to divide?"))

print(f"The result of division is {num1/num2: .2f}")





num1= float(input("Enter the first number you want to divide?"))
num2= float(input("Enter the second number you want to divide?"))

print(f"The result of division is {num1/num2: .6f}")



num1= float(input("Enter the first number you want to divide?"))
num2= float(input("Enter the second number you want to divide?"))

print(f"The result of division is {num1/num2: .6e}")










































































