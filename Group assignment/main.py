#i)
#Importing our module
import module

#Some information about the program
print("Welcome, this is the main python file. "
"\nThis is a group assignment which contains functions for Data cleaning, Data analysis tools and organizing code\n")

# Creating a menu with 3 options
# takes user input and converts it to a int
userInput = input("Type 1 to re-import and clean data\n"
"Type 2 to print a list of all companies, with their XDC\n"
"Type 3 to print information for a specified company. Hit enter to quit. ")

if userInput == "":
    print("Goodbye")
elif int(userInput) == 1:
    print("Now running function a, b, c, d: \n")
    print("Now running function: a")
    module.function_a()
    print("Now running function: b")
    module.function_b()
    print("Now running function: c")
    module.function_c()
    print("Function d creates a xdc.txt file")
    module.function_d()
elif int(userInput) == 2:
    print("Now running function: f")
    print("Printing a list of all companies, with their XDC: \n")
    module.function_f()
elif int(userInput) == 3:
    print("Now running function g: ")
    module.function_g()

