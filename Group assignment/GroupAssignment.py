#Section 1 (Weightage: 15 Percentage)
import random

#1

userInput = int(input("How many drinks do you usually have on a night out? "))

if userInput <= 3:
    print("Weakling")
elif userInput in range(4,11):
    print("Not bad...")
elif userInput > 10:
    print("Viking!")   


#2

for i in range(0,21):
    if i % 2 == 0:
        print(f"Even numbers: {i}")

#3

list = []

for i in range (6):
   randomInt = random.randint(1,30)
   list.append(randomInt)


print(list)


#4

def isPalindrome():
    user_input = input("Insert a word: ")
    if user_input[::-1] == user_input:
        return True
    else:
        return False
    
print(isPalindrome())

# Section 2 (Weightage: 85 Percentage)

# a) - data cleaning

#We made empty lists to store the columns
isin_company = []
marketValue = []
currency = []
assetClass = []
xdc = []
isin = []
company = []

lists = isin, company, marketValue, currency, assetClass, xdc

#The functions A, B and C is to answer task E
def function_a():
    #Opening the textfile
    text_file = open("Group assignment/xdc_companies_mac.txt", "r")
#We used a for loop to split the columns by commas
    for line in text_file:
        column = line.split(",")
        isin_company.append(column[0])
        marketValue.append(column[1])
        currency.append(column[2])
        assetClass.append(column[3])
        xdc.append(column[4])
#Closing file to save adjustments
    text_file.close()
    #printing to test out function, and seperating lines so it looks more clean when printed
    print(*isin_company, sep="\n ")


# b)

def function_b():
    with open("Group assignment/xdc_companies.txt", "r") as text_file:
        #We used the function replace to split isin and company, we thought this was the easiest way as we 
        #already split the lines with split(",")
        content = text_file.read().replace("_", ",")
        lines = content.splitlines()

#adding isin as a seperate column, and therefore the index numbers change
        for line in lines:
            column = line.split(",")
            isin.append(column[0])
            company.append(column[1])
            marketValue.append(column[2])
            currency.append(column[3])
            assetClass.append(column[4])
            xdc.append(column[5])

#printing to check that they are seperated
    print(*isin, sep="\n ")
    print(*company, sep="\n ")


# c)

def function_c(): 
    input_file=open("Group assignment/xdc_companies.txt", "r")
    content = input_file.read().replace("_", ",").replace("°C", "")
    lines = content.splitlines()

    for line in lines:
        parts=line.split(",")
        xdc.append(parts[5])
    
    print(xdc)
 


def function_d():
    input_file = open("Group assignment/xdc_companies_mac.txt", "r")
    output_file = open("Group assignment/xdc.txt", "w")
    lines = input_file.readlines()

    for line in lines:
        line = line.replace("_", ",")
        parts = line.split(",")
        output_file.write(f"{parts[0]}\n{parts[1]}\n{parts[2]}\n{parts[3]}\n{parts[5]}\n")
    
    input_file.close()
    output_file.close()


# e) oppgave a, b og c er hver sin egen funksjon. Kan sikkert endre på dette senere og ha alt i en funksjon

# Data analysis tool

# f) Hvis company name + XDC i terminal
def function_f():
        with open("Group assignment/xdc_companies.txt", "r") as text_file:
            content = text_file.read().replace("_", ",")
            lines = content.splitlines()

            for line in lines:
                column = line.split(",")
                isin.append(column[0])
                company.append(column[1])
                marketValue.append(column[2])
                currency.append(column[3])
                assetClass.append(column[4])
                xdc.append(column[5])

#We used dictionaries to connect each column
            companies={
                f"{company[0]}":f"{xdc[0]}",
                f"{company[1]}":f"{xdc[1]}",
                f"{company[2]}":f"{xdc[2]}",
                f"{company[3]}":f"{xdc[3]}",
                f"{company[4]}":f"{xdc[4]}",
                f"{company[5]}":f"{xdc[5]}",
                f"{company[6]}":f"{xdc[6]}",
                f"{company[7]}":f"{xdc[7]}",
                f"{company[8]}":f"{xdc[8]}",
                f"{company[9]}":f"{xdc[9]}",
                f"{company[10]}":f"{xdc[10]}"
                }

        print(companies) 
    

def function_g():
    
    data = {}
    userInput = input("Which company would you like to see the data for? ")

    with open("Group assignment/xdc_companies.txt", "r") as textFile:
        lines = textFile.readlines()

        for line in lines:
            line = line.replace("_", ",")
            section = line.strip().split(",")

            isin = section[0]
            company = section[1]
            marketValue = section[2]
            currency = section[3]
            assetClass = section[4]
            xdc = section[5]


            data[company] = {
                "ISIN" : isin,
                "Market Value" : marketValue,
                "Currency" : currency,
                "Asset class" : assetClass,
                "xdc" : xdc
            }

        while userInput not in data:
            print("Could not find company that you are asking for, please try again")
            userInput = input("Which company would you like to see the data for? ")

        print(f"Data for {userInput} : {data[userInput]}")

