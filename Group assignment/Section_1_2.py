#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 12:50:01 2025

@author: piaavitsland
"""
"""
#%%
#1
customer= int(input("How many drinks do you have per week?"))

#%%
#2

abc = 17%3 
print(abc)

#range henter alle tallene i tuplene.
for i in range (0,21):
    if i % 2 == 0:
        print (f"Even numbers: {i}")

#%%
#3
#første du må gjøre er å importere det du skal.

import random 

#lag en tom liste
list = []

for numbers in range(1,7):
    varRandom=random.randint(1,30)
    list.append(varRandom)
    
print(list)

#%%
#4

def ifPalindrome():
    user_input=input("Give me a word: ")
    if user_input == user_input[::-1]:
        return True
    else:
        return False 

print(ifPalindrome())







input_file=open("xdc_companies_mac.txt", "r")
lines=input_file.readlines()
print(lines)









#%%


#5
#a) 

isin_company = []
market_value = []
currency = []
xdc = []


input_file=open("xdc_companies_mac.txt")

#e)
def function_a(): 
    input_file=open("xdc_companies_mac.txt", "r")
    lines=input_file.readlines()

    for line in lines:
        parts = line.split(",")
        isin_company.append(parts[0])
        market_value.append(parts[1])
        currency.append(parts[2])
        xdc.append(parts[3])
        print(isin_company)


    input_file.close()

#b

isin=[]
company=[]
def function_b(): 
    input_file=open("xdc_companies_mac.txt", "r")
    content=input_file.read().replace("_", ",")
    lines=content.splitlines()


    for line in lines:
        parts=line.split(",")
        isin.append(parts[0].upper())
        company.append(parts[1].upper())
    

    print(parts)

    input_file.close()

    print(isin)
    print(company)

"""
#c)


  
isin=[]
company=[]
market_value = []
currency = []
xdc = []

def function_c(): 
    print("This is function C: \n")
    input_file=open("xdc_companies_mac.txt", "r")
    content = input_file.read().replace("_", ",").replace("C", "")
    lines = content.splitlines()

    for line in lines:
        parts=line.split(",")
        isin.append(parts[0].upper())
        company.append(parts[1].upper())
        market_value.append(parts[2])
        currency.append(parts[3])
        xdc.append(parts[5])
    


    print(xdc)



    input_file.close()

"""
#d)
isin = []
company = []
market_value = []
currency = []
xdc = []

input_file = open("xdc_companies_mac.txt", "r")

for line in lines:
    parts=line.split(",")
    isin.append(parts[0].upper())
    company.append(parts[1].upper())
    market_value.append(parts[2])
    currency.append(parts[3])
    xdc.append(parts[5])

with open("xdc.txt", "w") as output_file:
    # Write the header (optional)
  output_file.write(f"{isin},{company},{market_value},{currency},{xdc}\n")
 
output_file.close()   
"""

#e)
dict1={}
function_c()



def function_f(): 
    companies={f"{company[0]}":f"{xdc[0]}",
               f"{company[1]}":f"{xdc[1]}",
               f"{company[2]}":f"{xdc[2]}",
               f"{company[3]}":f"{xdc[3]}",
               f"{company[4]}":f"{xdc[4]}",
               f"{company[5]}":f"{xdc[5]}",
               f"{company[6]}":f"{xdc[6]}",
               f"{company[7]}":f"{xdc[7]}",
               f"{company[8]}":f"{xdc[8]}",
               f"{company[9]}":f"{xdc[9]}",
               f"{company[10]}":f"{xdc[10]}"}

    print(companies) 
               
    
input_file=open("xdc_companies_mac.txt", "r")

#function_f()

#def function_g():
#    userinput = input("Please write a company name: ")