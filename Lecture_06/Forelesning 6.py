#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 08:43:26 2025

@author: kamillakjaer
"""

input_file = open("myfile.txt", "r")

lines = input_file.readlines()
print(lines)

#Fikk ikke fullført fordi jeg kom for seint
path = r"C:"
file_name = "myfile.txt"


#Read the file

input_file2 = open(path + file_name, "r")
input_file2.readlines()


type(lines)
len(lines)


lines[2]

input_file.close()


#For loop

input_file = open("myfile.txt", "r")

for line in input_file:
    print(line, end = "")
input_file.close()

#Read

input_file = open("myfile", "r") 
input_file.read() 
input_file.close()



#Write a file

output_file = open("myfile2.txt", "w")

output_file.write("I wrote this line.\n")
output_file.write("I wrote this 2nd line. \n")


output_file.close()


#Appending new text, the a instead of the w behind "myfile2.txt" adds like the function append

output_file = open("myfile2.txt", "a")

output_file.write("I wrote this 3nd line. \n")
output_file.write("I wrote this 4nd line. \n")

output_file.close()



#Transferring things from one file to another

input_file = open("myfile.txt", "r")

output_file = open("myfile_new.txt", "w")
#You can not use a w on a allready existing file, it will just delete the file for a new, you need to use an a to add to the file


for line in input_file:
    output_file.write(line)

input_file.close()
output_file.close()

#Have to remember to close the file to save the changes that are made


#%%

#String traversal

input_file = open("myfile.txt", "r")

for line in input_file:
    length = len(line)
    print(f"The length of the line: {length}")
    
input_file.close()
    
    
#If you want to count the number of spaces in each line

input_file = open("myfile.txt", "r")

#for line in input_file:
    #num_space = 0
   # for char in line:
       # if char == " ":
            
            

#%%

#Oppgave A1, 2, 3, 4

path = r"/Users/kamillakjaer/Downloads"
input_file = open("poem.txt", "r")  

poem_lines = input_file.readlines()
print(poem_lines)

for line in input_file:
    print(line, end = "")
        

input_file = open("poem.txt", "r")
input_file.readline()
input_file = open("poem.txt", "r")
input_file.readlines()



#Oppgave A5

output_winston = open("winston.txt", "w")
output_winston.write("Success is not final. \n")
output_winston.write("failure is not fatal. \n")
output_winston.write("It is the courage to continue that counts. \n")

output_winston.close()


#%%

#Modules

"""
pandas - data analysis
matplotlib - plot
math - specialised math function
numpy - arrays
"""


import math

math.exp(44)

"2dn way to import a module"
import math as mm

mm.exp(44)


#Will be creating functions through creating your own module


def display_greetings():
    print("Hie, how are you?")
    
    
def Hello_teller() :
    print("Hi, Hello?")
    












