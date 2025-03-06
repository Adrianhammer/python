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

lists = isin_company, marketValue, currency, assetClass, xdc, isin, company


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
    print(*isin_company, sep="\n ")


# b)



def function_b(value):
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


# c)
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


    with open("Group assignment/xdc.txt", "w") as new_file:
        for list in lists:
            for word in list:
                new_file.write("%s\n" % word)

    #print(*value, sep="\n ")

function_c()