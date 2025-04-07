import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Oppgave 1

import random


def generate_password():
    password_length = int(input("Give a number between 15 and 20 to decide the length of your password"))
    password = ""
    characters = (r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRZTUVWXYZ!@#-_.,:;()=?\/")
    if password_length < 15 or password_length > 20:
        password_length = int(input("Invalid! Enter a number between 15 and 20: "))
    else:
        True
        
    for i in range(password_length):
        password += random.choice(characters)
   #slet med å finne filen og om den ble lagd     
    with open("password.txt", "w") as file:
        file.write(f"This is your password: {password}")

        print(password)
    
generate_password()

# Oppgave 2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#a)

orders = pd.read_csv('orders.csv')
print(orders.head())

#b)

products = pd.read_excel('products.xlsx')
print(products.head())

#c) Merge orders and products using "product_id" as the common column

result = orders.merge(products, on = 'product_id')
print(result.head())

#d) drop rows with NaNs

result.dropna(inplace = True)
print(result)

#e) Create a new variable called "order_cost", which is the product amount multiplied with product cost

result['order_cost'] = result['units_sold'] * result['product_cost']
print(result)

# Oppgave 3

#3
#a)
print(result.describe())

#b) 
result['month'] = pd.to_datetime(result['month'], format='%Y-%m')
# Filtrer data for hvert produkt basert på product_id
mac_df = result[result["product_id"] == 1001]
lenovo_df = result[result["product_id"] == 1002]
iphone_df = result[result["product_id"] == 1003]
samsung_df = result[result["product_id"] == 1004]

# Beregn korrelasjonskoeffisientene
corr_mac = mac_df.corr().loc["sales_price_per_unit", "units_sold"]
corr_lenovo = lenovo_df.corr().loc["sales_price_per_unit", "units_sold"]
corr_iphone = iphone_df.corr().loc["sales_price_per_unit", "units_sold"]
corr_samsung = samsung_df.corr().loc["sales_price_per_unit", "units_sold"]


# Opprett subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
fig.suptitle("Price vs Quantity Sold")

# Plot Macbook Air
axes[0, 0].scatter(mac_df["sales_price_per_unit"], mac_df["units_sold"])
axes[0, 0].set_title(f"Macbook Air (r = {corr_mac:.2f})")
axes[0, 0].set_xlabel("Price")
axes[0, 0].set_ylabel("Quantity")

# Plot Lenovo Thinkpad
axes[0, 1].scatter(lenovo_df["sales_price_per_unit"], lenovo_df["units_sold"])
axes[0, 1].set_title(f"Lenovo Thinkpad (r = {corr_lenovo:.2f})")
axes[0, 1].set_xlabel("Price")
axes[0, 1].set_ylabel("Quantity")

# Plot iPhone 14
axes[1, 0].scatter(iphone_df["sales_price_per_unit"], iphone_df["units_sold"])
axes[1, 0].set_title(f"iPhone 14 (r = {corr_iphone:.2f})")
axes[1, 0].set_xlabel("Price")
axes[1, 0].set_ylabel("Quantity")

# Plot Samsung Galaxy S22
axes[1, 1].scatter(samsung_df["sales_price_per_unit"], samsung_df["units_sold"])
axes[1, 1].set_title(f"Samsung Galaxy S22 (r = {corr_samsung:.2f})")
axes[1, 1].set_xlabel("Price")
axes[1, 1].set_ylabel("Quantity")

plt.show()


# Oppgave 4

#4a)

result['revenue'] = result['units_sold']*result['sales_price_per_unit']
revenue_per_product = result.groupby('product_name')['revenue'].sum()
print(revenue_per_product)

fig, ax = plt.subplots()
ax.bar(['Iphone 14', 'Lenovo Thinkpad', 'Macbook Air', 'Samsung Galaxy S22'], revenue_per_product)

ax.set_title('The revenue for each product')
ax.set_xlabel('Product ID')
ax.set_ylabel('Total Revenue')

plt.show()

#4b)
# filtering rows with Mac

Iphone = result[result['product_name'] == 'Iphone 14']
Lenovo = result[result['product_name'] == 'Lenovo Thinkpad']
Macbook = result[result['product_name'] == 'Macbook Air']
Samsung = result[result['product_name'] == 'Samsung Galaxy S22']

fig, ax = plt.subplots(nrows = 1, ncols = 4)


ax[0].hist(Iphone,)
