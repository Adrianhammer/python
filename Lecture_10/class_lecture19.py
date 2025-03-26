# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:35:58 2024

@author: basiv7626
"""

import pandas as pd

grade_dict = {'Name' : ['Jenny', 'Oleg', 'Chang', 'Jonas'],
              'Score' : [95.0, 79.0, 58.0, 71.0],
              'Pass' : ['yes', 'yes', 'no', 'yes'],
              'Age'   : [19, 18, 20, 22], 
              'City'  : ['Bergen', 'Oslo', 'Copenhagen', 'Stockholm']
             }

df= pd.DataFrame(grade_dict)

pass_group= df.groupby("Pass")

pass_group.mean()
pass_group.sum()
pass_group.max()
pass_group.min()
pass_group.count()


#%%

titanic= pd.read_csv("titanic.csv")

titanic.columns

pclass_group= titanic.groupby("Pclass")

pclass_group["Survived"].value_counts()

pclass_sex_group= titanic.groupby(["Pclass", "Sex"])

pclass_sex_group["Survived"].mean()

#%%

#Correlation Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x= np.arange(10, 70, 10 )
x
y= [38, 22, 20, 14, 12, 5]

fig, ax= plt.subplots()
ax.scatter(x, y)

np.corrcoef(x,y)

values = {"Price": np.arange(5, 60, 10),
          "Demand": [38, 22, 20, 14, 12, 5]}


data= pd.DataFrame(values)

fig, ax= plt.subplots()
ax.scatter(data["Price"],data["Demand"])
ax.set_xlabel("Price")
ax.set_ylabel("Demand")

data.corr()

data.corr().loc["Demand"]

#%%

#Vectorization
"""
A1. Make 2 million random draws from a 
uniform distribution. Sum them
up by using a for-loop. 
How long does it take to run the code?
"""

import random
import time


start = time.time()

empty_list=[]

for i in range(1_000_000):
    x= random.uniform(0, 10)
    empty_list.append(x)

sum(empty_list)

end= time.time()

print(end-start)

"""
A2. Make 2 million random draws from a uniform distribution. Sum them
up by using the numpy sum function. How long does it take to run the
code?
"""

import numpy as np
start = time.time()
z= np.random.uniform(0, 10, 1_000_000)
sum_z= np.sum(z)
end= time.time()
print(end-start)

#%%

def name_fn():
    import numpy as np
    start = time.time()
    z= np.random.uniform(0, 10, 1_000_000)
    sum_z= np.sum(z)
    end= time.time()
    print(end-start)


x= {"Toyota": [1233, "Yen", "3.6"]}

comp= input("Please enter the name of the firm? ")
x[comp]

#%%

data= pd.read_csv("mpg.csv")

data
"""
n the first subplot, create a scatter plot of mpg and horsepower.
- In the second subplot, create a scatter plot of mpg and weight.
- In the third subplot, create a scatter plot of mpg and acceleration
"""

data.columns

fig, ax= plt.subplots(1, 3)
ax[0].scatter(data["mpg"], data["horsepower"])
ax[1].scatter(data["mpg"], data["weight"])


#%%

"""
A4. Create a figure with three subplots:
- In the first subplot, create a bar plot of
 average mpg by origin.
- In the second subplot,
 create a bar plot of average mpg by year.
- In the third subplot,
 create a bar plot of average mpg by cylinders.

"""
origin= data.groupby("origin")["mpg"].mean()
year= data.groupby("model_year")["mpg"].mean()

fig, ax= plt.subplots(1,2)
ax[0].bar(origin.index, origin)
ax[1].bar(year.index, year)

