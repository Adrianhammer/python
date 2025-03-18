#Oppgave 2 a)

isin_company = []
Market_Value = []
Currency = []
xdc = []

text_file = open('/Users/kamillakjaer/downloads/xdc_companies_mac.txt', 'r')
lines = text_file.readlines()
print(lines)

for line in lines:
    parts = line.split("\t")
    isin_company.append(parts[0])
    Market_Value.append(parts[1])
    Currency.append(parts[2])
    xdc.append(parts[3])
    print(isin_company)

text_file.close()

