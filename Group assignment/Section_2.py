# Nå begynner jeg med del 2 av oppgaven
#2

# a) - data cleaning oppgave
text_file = open("Group assignment/xdc_companies_mac.txt", "r")


isin_company = []
marketValue = []
currency = []
assetClass = []
xdc = []

for line in text_file:
    column = line.split(",")
    isin_company.append(column[0])
    marketValue.append(column[1])
    currency.append(column[2])
    assetClass.append(column[3])
    xdc.append(column[4])

print(*isin_company, sep="\n ")