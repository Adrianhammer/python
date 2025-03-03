#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 10:34:36 2025

@author: kamillakjaer
"""

def fact() :
    print("This is my factorial function!")
    

import math as mth

def fact2(n) :
    empty_list = []
    for i in range(1, n + 1):
        x = (n + 1)- i
        empty_list.append(x)
    return mth.prod(empty_list)



#%%


# isdigit function checks if a variable has digits, can be used if you have variables
# with a mix of numbers and other inputs


# function find can be used to find the index position of a particular sign or part of a string


# function split splits a string where you want it to

email_id = "name_surname@abc.com"
Websites = email_id.split("@")

email_id.replace("abc.com", "gmail.com")

word1 = "cotton"

word1.replace("tt", "mm")

Websites[1]

email_id = "name_surname@abc.com"

email_id.replace("name", "alex").upper()

email_id.replace("name", "alex").upper().isdigit()


#%%

#A4

line = "This is my string, you see"
line1 = line.split(",")
print(line1 [0])
print(line1 [1])


#A5

name_file = open("babynames2000s.txt" , "r")
name_file.readlines()


















