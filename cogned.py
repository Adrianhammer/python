isin_company = []
marketValue = []
currency = []
assetClass = []
xdc = []
isin = []
company = []

lists = isin, company, marketValue, currency, assetClass, xdc

# c)

def function_c(): 
    input_file=open("Group assignment/xdc_companies_mac.txt", "r")

    #Here we also found it easier to just replace the °C with blank 
    #since this was the only character which was not float
    content = input_file.read().replace("_", ",").replace("°C", "")
    lines = content.splitlines()

    #We did not add the other columns as we only needed to adjust the xdc
    for line in lines:
        parts=line.split(",")
        xdc.append(parts[5])
    
    print(xdc)
 

#d)
def function_d():
    input_file = open("Group assignment/xdc_companies_mac.txt", "r")
    #Making a new file
    output_file = open("Group assignment/xdc.txt", "w")
    #Seperating the lines into lists
    lines = input_file.readlines()

    for line in lines:
        line = line.replace("_", ",")
        parts = line.split(",")
        #Adding the different parts to the output file and seperating each part
        output_file.write(f"{parts[0]}\n{parts[1]}\n{parts[2]}\n{parts[3]}\n{parts[5]}\n")
    
    input_file.close()
    output_file.close()


# e) As you can see over, we have made a, b and c into seperate functions


# Data analysis tool

# f) 
def function_f():
        #Found out that we could use with open so we didn`t have to close file every time
        with open("Group assignment/xdc_companies_mac.txt", "r") as text_file:
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

#We used dictionaries to connect each column of company and xdc
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
    

#g)
def function_g():
    #Empty dictionary
    data = {}
    userInput = input("Which company would you like to see the data for? ")

    with open("Group assignment/xdc_companies_mac.txt", "r") as textFile:
        lines = textFile.readlines()

        for line in lines:
            line = line.replace("_", ",")
            #Using strip to remove spaces at the beginning and end of string
            section = line.strip().split(",")


            isin = section[0]
            company = section[1]
            marketValue = section[2]
            currency = section[3]
            assetClass = section[4]
            xdc = section[5]

            # In this dictionary the company is the key while isin, marketvalue, currency, assetclass and xdc are values
            data[company] = {
                "ISIN" : isin,
                "Market Value" : marketValue,
                "Currency" : currency,
                "Asset class" : assetClass,
                "xdc" : xdc
            }

        # Checking if the user writes a company that is in the dictionary. If it is not the user is asked again to input a company
        while userInput not in data:
            print("Could not find company that you are asking for, please try again")
            userInput = input("Which company would you like to see the data for? ")

        #Prints the user input which will be a company name and the data for that company
        print(f"Data for {userInput} : {data[userInput]}")


