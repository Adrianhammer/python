# You can summarize allot of data by using the function groupby and value_counts
# Summarizes data based on a particular column

# Instead of value_vount you can use mean() to summarize the information

# Merge - merges two files together, combines horisontally, the data is combined side by side
# Concat - helps combine two files vertically, it stacks the data on top of each other

# When combining two lists with concat, it can look messy because it does not adjust any data
"""
#merging
x = df1.merge(df2, on = "Name")

x.head(3)

# The left comment adds data even though its not in both lists

df1.merge(df2, on = "Name", how = "left")


# The comment outer merges all the rows together

# How to visualize data frames using pandas
# Making a histogram based on data from titanic file, (jeg husker ikke hvordan jeg legger inn en ny fil)

titantic3.hist(column = "fare")


# Can use matplotlib to plot extra spots in graph or histogram

# Creating different historgrams to split who survived and not during titantic
import pandas as pd


# Oppgave A1

titanic = pd.read_csv ("Lecture_09/titanic(1).csv")

titanic.value_count()

missing_age = titanic["Age"].isnull().sum()


# Oppgave A3

import matplotlib.pyplot as plt

mpg = pd.read_csv("mpg.csv")
fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (13, 3))

ax[0].scatter((mpg["Horsepower"], ["mpg"]))
ax[1].scatter(mpg["Weight"], ["mpg"])
ax[2].scatter(mpg["Acceleration"], ["mpg"])


# Lists

my_list = [1, 2, 3, 4]

print(type(my_list))

list3 = [8, 9, 10]

list4 = list3.sort()

list3.append()


# Class and objects in python
# Class as a baking mold, within the list the mold makes different shapes which can contain different ingredients
# To create your own class

class Business:
    def __init__(self, initial_account):
        self.bank = initial_account

    def sale(self, sale):
        self.bank_account = self.bank_account + sale
    

Thon_properties = Business(1000)

print(Thon_properties)

"""
# A1 og A2

class Stock:
    def __init__(self, initial_stock_price):
        self.stock_price = initial_stock_price
    

        

FRO = Stock([166.6, 167.08, 167.14, 173.12, 173.36])




        
