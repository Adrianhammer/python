import module

print("Welcome, this is the main python file. "
"\nThis is a group assignment which contains functions for Data cleaning, Data analysis tools and organizing code\n")

userInput = int(input("Type 1 to re-import and clean data\n"
"Type 2 to print a list of all companies, with their XDC\n"
"Type 3 to print information for a specified company. Hit enter to quit. "))

if userInput == 1:
    print("Now running function a, b, c, d: \n")
    module.function_a()
    module.function_b()
    module.function_c()
    module.function_d()
elif userInput == 2:
    print("Printing a list of all companies, with their XDC: \n")
    module.function_f()
elif userInput == 3:
    print("Now running function g: ")
    module.function_g()

