#Correlation - the correlation between two object measured between -1 and 1
#Example - the warmer weather the more ice cream is sold
#Can use scatterplot to show data on correlation
#To know exact correlation:
# np.corrcoef(x, y)

#Second method:
# pandas module with df.corr() - function

# If you dont want to know the correlation between all the variables you can specify it with a list

# Simple regression - you want to analyse the relationship between two variables: one independent and one dependent
# Slope (beta1): the change in the dependent variable when one change in the independent variable

# The fit function to create a model
# Describe model: model = sm.OLS(Y,X) (Y is the dependent variable, and X is the independent variable)
# Fit model: reg_res = model.fit()

#A1
"""
In this exercise, use the file "wage.csv".
This file contains data on the following variables:
• wage – hourly wage in kroners
• hours – hours worked per week
• IQ - intelligence quotient
• educ - years of education
• exper - years of experience
A1. Import "wage.csv" and put the data into a
Pandas data frame.
"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


wage = pd.read_csv("wage.csv")

print(wage.corr())




#A3

"""
A3. Make a figure with three plots:
1. wage vs. hours
2. wage vs. educ
3. wage vs. exper
Do you think any of these variables can explain the variance seen in hourly wage?
"""

1.
wage = pd.read_csv("wage.csv")

ax[0].scatter(wage["hours"], wage["wage"])
ax[0].set_ylabel("wage")
ax[0].set_xlaber("hours")
ax[0].set_title("r = " + str(round(corr_hours, 2)))




#A4

"""
A4. Make the following regressions:
1. wage vs. hours
2. wage vs. educ
3. wage vs. exper
Which of the right-hand variables (hours, educ, exper)
explain more of the variance of hourly wage?
"""

1.
wage = pd.read_csv("wage.csv")

Y = wage["wage"]
X = wage["hours"]
X = sm.add_constant(data = X)

model = sm.OLS(Y, X)
reg_res = model.fit()
print("The r-squared of wage on hour is; " +str(round(res1.rsquared, 2)) + "")



# beta coeffisient for education
res1.params["educ"]

# estimate wage
estimated_wage = res1.params["const"] + res1.params["educ"] * years_educ


# with add_constant(X) function you will line up the regression line with X


"""
A1. Use the DataFrame mpg, and estimate the regression model,
= + 1 + 2𝑚𝑝𝑔 𝛼 𝛽 ℎ𝑜𝑟𝑠𝑒𝑝𝑜𝑤𝑒𝑟 𝛽 𝑤𝑒𝑖𝑔ℎ𝑡
, as in the lecture.
However, this time, plot the regression line between
and , while assuming that is𝑚𝑝𝑔 𝑤𝑒𝑖𝑔ℎ𝑡 ℎ𝑜𝑟𝑠𝑒𝑝𝑜𝑤𝑒𝑟
equal to its mean value in the data.
"""
mpg = pd.read_csv('mpg.csv')

# drop nans, dropping things without value
mpg.dropna(inplace = True)
# extract X and Y variables
X = mpg[['horsepower', 'weight']]
Y = mpg['mpg']
### Create model
# add constant
X = sm.add_constant(X)
# fit model
model = sm.OLS(Y, X).fit()
### Make predictions
# copy df
X3 = X.copy()
# calculate mean weight
hp_mean = mpg['horsepower'].mean()
# set weight equal to its mean
X3['horsepower'] = hp_mean
# sort
X3.sort_values('weight', inplace = True)
# predict and add to df
pred3 = model.predict(X3)
mpg['Pred3'] = pred3
### Plot
fig, ax = plt.subplots()
# plot actual mpg
ax.scatter(mpg['weight'], mpg['mpg'], label = 'Actual mpg')
# plot predicted mpg
ax.plot(mpg['weight'], mpg['Pred3'], color = 'black', label = 'Regression line')
# add title and labels
ax.set_title(f'horsepower = {hp_mean:.2f}')
ax.set_ylabel('mpg', fontsize = 14)
ax.set_xlabel('weight', fontsize = 14)
# add legend
ax.legend()
plt.show()



