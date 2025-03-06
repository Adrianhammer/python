# Nå begynner jeg med del 2 av oppgaven
#2

# a) - data cleaning oppgave


isin_company = []
marketValue = []
currency = []
assetClass = []
xdc = []
isin = []
company = []

lists = isin, company, marketValue, currency, assetClass, xdc


def function_a():
    text_file = open("Group assignment/xdc_companies_mac.txt", "r")

    for line in text_file:
        column = line.split(",")
        isin_company.append(column[0])
        marketValue.append(column[1])
        currency.append(column[2])
        assetClass.append(column[3])
        xdc.append(column[4])

    text_file.close()
    #print(*isin_company, sep="\n ")


# b)

def function_b():
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


    #print(*isin, sep="\n ")
    #print(*company, sep="\n ")


# c) Fikser denne senere slik at text filen blir bedre skrevet til (vertikale kolonner istedenfor horisontale)
def function_c():
    with open("Group assignment/xdc_companies.txt", "r") as text_file:
        content = text_file.read().replace("_", ",").replace("°C", "")
        lines = content.splitlines()

        for line in lines:
            column = line.split(",")
            isin.append(column[0])
            company.append(column[1])
            marketValue.append(column[2])
            currency.append(column[3])
            assetClass.append(column[4])
            xdc.append(column[5])


def function_d():
    with open("Group assignment/xdc.txt", "w") as new_file:
        for list in lists:
            new_file.write(f"{list}\r\n")

#function_a()
#function_b()
function_c()
function_d()
# e) oppgave a, b og c er hver sin egen funksjon. Kan sikkert endre på dette senere og ha alt i en funksjon

# Data analysis tool

# f) Hva mener han med denne oppgaven? Mener han lese fra filen vi lagde i oppgave d? eller fra listene
#    "[...] in your data" er ganske vagt

# g) 

def function_g():
    user_input = input("Which company would you like to see the data for? ")

    while user_input not in company:
        print("Please write another company")
        user_input = input("Which company would you like to see the data for? ")
    print("great")
    


function_g() 
