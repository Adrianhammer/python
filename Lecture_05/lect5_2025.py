# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 08:29:16 2025

@author: basiv7626
"""

"""Basic function"""

def print_something():
    print("This is a fucntion that prints something")
    
print_something()


#Function that accepts an argument

def number_displayer(number):
    print(f"The number you typed is {number}")
    
number_displayer(26)    


def return_number(n):
    return n


x = return_number(5)
x


def return_number_with_print(n):
    print(n)

y= return_number_with_print(6)

y
#%%

""" The task if to find the mean or averga of a list """

inputed_list= [2,4,5,6]

list_sum= sum(inputed_list)

len_list= len(inputed_list)

avg_list= list_sum/len_list

print(f"The average of the list is {avg_list}")

def avg_list_fn(number_list):
    list_sum= sum(number_list)
    len_list= len(number_list)
    avg_list= list_sum/len_list
    return avg_list


avg_list_fn([4,56,7,4])
avg_list_fn([4,5,6,9])

def avg_list_print(number_list):

    # sum the list of numbers
    list_sum = sum(number_list)

    # lenght of the list
    list_length = len(number_list)

    # calculate the mean
    mean = list_sum / list_length
    
    # print mean
    return mean

y = avg_list_print([2,3,4])

   
#%%

def hi_printer():
    print("Hi everybody!")

hi_printer()


def age_printer(n):
    print(f"You are {n} years old")

age_printer(55)


def my_square(n):
    sq_n= n**2
    return sq_n


def even_number_printer(n):
    even_list=[]
    for i in range(0, n, 2):
        even_list.append(i)
    
    return even_list

even_number_printer(33)



def even_number_printer_while(n):
    even_list=[]
    i=1
    while i*2<=n:
        even_list.append(i*2)
        i=i+1
    return even_list
    
even_number_printer_while(33)


#%%



def avg_list_print(number_list):

    # sum the list of numbers
    list_sum = sum(number_list)

    # lenght of the list
    list_length = len(number_list)

    # calculate the mean
    mean = list_sum / list_length
    
    # print mean
    return mean

#Otion 1
avg_list_print([2,45,6,5])

#Option2
input_list= [2,4,567,6]
avg_list_print(input_list)

#Option 3
avg_list_print(number_list = input_list)



def exp(base, exponent = 2): # default: square base
    result = base**exponent
    return result


exp(2)

sum([exp(10, 3), 2, 3, 4, 5, 6, 7, 8, 9])



n = -10
res = change_value(n=5)
res
print(n)

def change_value(n):
    if n < 0:
        n = 0
    return n


def change_list(num_list):
    for k in range(len(num_list)):
        if num_list[k] < 0:
            num_list[k] = 0
            
    return num_list

int_list = [5, -2, 9, 4, -6, 1]

res = change_list(int_list)
res
int_list


#%%

def stock_price(dividends, interest_rate, growth_rate):
    price= dividends/(interest_rate-growth_rate)
    return price


stock_price(100, 5.5, 3)
"""
A2. Call the function from A1 both with positional arguments and with
keyword arguments.
"""

"""stock_price(dividends, interest_rate, growth_rate)"""

stock_price(100, 5.5, 3)

stock_price(dividends= 100, growth_rate=3,interest_rate= 5.5)


def stock_price(dividends, interest_rate, growth_rate):
    price= dividends/(interest_rate-growth_rate)
    return price


"""Local Variables and Global Variables"""

print(stock_price(20,12,3))

print(price)
price= 55


def stock_price(dividends, interest_rate, growth_rate):
    list1.append(dividends/(interest_rate-growth_rate))
    return list1

list1=[3,45,6]

print(stock_price(20,12,3))
list1
#%%


def stock_price(dividends, interest_rate= 0.3, growth_rate=0.5):
    price= dividends/(interest_rate-growth_rate)
    return price

stock_price(1.85)



def printAsterisks(n):
    if n<75:
        print("*"*n)
    else:
        print("*"*75)
    
printAsterisks(2)


#%%

def stock_price(dividends, interest_rate= 0.3, growth_rate=0.5):
    price= dividends/(interest_rate-growth_rate)
    return price


def main():
    print("This function gives you the stock price")
    dividend= int(input("Please enter the dividend? "))
    interest_rate= int(input("Enter interest? "))
    growth_rate= int(input("Enter growth? "))
    
    
    print(f"The stock price is {stock_price(dividend,interest_rate,growth_rate)}")
    

main()




def addVegetable(veg_name, veg_set):
    if veg_name not in veg_set:
        veg_set.add(veg_name)
    else:


        print(f'{veg_name} already exists.')


#Main part of the code
veg_set=set()
def main():
    veg_name= input("Please enter name of a veggie? ")
    
    
    while veg_name != '':
        
        # ...add to set
        addVegetable(veg_name, veg_set)
        
        # ...ask for next input
        veg_name = input('Enter another vegetable name (press Enter to quit):')
        

main()
    
print(veg_set)












