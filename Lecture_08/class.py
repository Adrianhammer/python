#Går igjennom fig, figurformel som basically lar oss lage en graf
#Vi har gått igjennom dette med å lage graf forrige uke da jeg var borte
#Bruker plot for å plotte alle stedene grafen skal igjennom

#fig, ax = plt.subplots()
#ax.plot(x, y, 'b-', linewidth = 2, label = 'sin(x)')


#To make scatterplots

#x_values = [1, 2, 3, 4, 5]
#y_values = [2, 4, 6, 8, 10]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values)

#plt.show()

#Skjønner ikke hvorfor det blir feil

date = []
bitcoin_price = []

BTC = open('/Users/kamillakjaer/downloads/BTC-USD.txt', 'r')
lines = BTC.readlines()
BTC.close()
lines = lines[1:]

for i in lines:
    line = i.split(',')
    date.append(line[0])
    bitcoin_price.append(float(line[1].replace('\n', '')))

print(bitcoin_price)

#Når du har åpnet teksten skal den splittes ved komma med for loops

#Oppgave A2
import matplotlib.pyplot as plt

attended = []
not_attended = []

prosent = open('/Users/kamillakjaer/downloads/percent_below_upper_secondary.txt', 'r')
linjer = prosent.readlines()
prosent.close()
linjer = linjer[1:]

for i in linjer:
    line = i.split(',')
    attended.append(line[0])
    not_attended.append(float(line[1].replace('\n', '')))

fig, ax = plt.subplots()
ax.hist(not_attend,
        )
#Fikk ikke gjort ferdig bc kan gikk fra fasit:((


unemp = [0.068,0.075,0.069,0.061,0.056,0.054,0.049,0.045,0.042,0.04,0.047,0.058,0.06,0.055,0.051,0.046,0.046,0.058,0.093,0.096,0.09,0.081,0.074,0.062,0.053,0.049]

infl = [0.04234964,0.030288197,0.02951657,0.026074416,0.028054197,0.029312042,0.023376899,0.015522791,0.021880272,0.033768573,0.028261711,0.015860316,0.02270095,0.02677236,0.033927468, 0.032259441,0.028526725,0.038391003, 0.003555463,0.016400434,0.031568416,0.020693373,0.014648327,0.01622223,0.001186271,0.012615832]

fig, ax = plt.subplots()
ax.scatter(unemp, infl)
ax.set_xlabel('unemployment')
ax.set_ylabel('inflation')


""" series is a single column of data, we can store two-dimensional data in a pandas DataFrame """

grade_dict = {name : [ "Fred", "Susanna", "Per"]}

"""Pandas are efficient when opening files"""

titanic = pd.read_csv

"""csv = comma seperated values"""
"""in special cases when the words are seperated by pipes instead of comma its important to seperate by pipes instead"""
""" data manipulation: you can filter rows and find average age etc"""
""" Axis = 0 stands for rows and Axis = 1 stands for rows"""


#Oppgave A1 (lecture 21)

#Use comment head, tail, info
import pandas as pd


car = pd.read_csv('/Users/kamillakjaer/downloads/mpg.csv')
print(car.head())
car.tail()
car.info()


mpg.to_excel(mpg.xlsx)






