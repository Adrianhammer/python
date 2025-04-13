import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Oppgave 1
#%%
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
    return password
    
generate_password()
#%%
# Oppgave 2

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#a)

orders = pd.read_csv('orders.csv')
print(orders.head())

#%%
#b)

products = pd.read_excel('products.xlsx')
print(products.head())

#%%

#c) Merge orders and products using "product_id" as the common column

result = orders.merge(products, on = 'product_id')
print(result.head())
#%%
#d) drop rows with NaNs

result.dropna(inplace = True)
print(result)
#%%

#e) Create a new variable called "order_cost", which is the product amount multiplied with product cost

result['order_cost'] = result['units_sold'] * result['product_cost']
print(f"here is {result}")
#%%
# Oppgave 3

#3
#a)
print(result.describe())

#%%
#b) 
#result['month'] = pd.to_datetime(result['month'], format='%Y-%m')
# Filtrer data for hvert produkt basert på product_id
mac_df = result[result["product_id"] == 1001]
lenovo_df = result[result["product_id"] == 1002]
iphone_df = result[result["product_id"] == 1003]
samsung_df = result[result["product_id"] == 1004]


# Beregn korrelasjonskoeffisientene
corr_mac = mac_df[["sales_price_per_unit", "units_sold"]].corr().loc["sales_price_per_unit", "units_sold"]
#corr_mac = mac_df.corr().loc["sales_price_per_unit", "units_sold"]
corr_lenovo = lenovo_df[["sales_price_per_unit", "units_sold"]].corr().loc["sales_price_per_unit", "units_sold"]
corr_iphone = iphone_df[["sales_price_per_unit", "units_sold"]].corr().loc["sales_price_per_unit", "units_sold"]
corr_samsung = samsung_df[["sales_price_per_unit", "units_sold"]].corr().loc["sales_price_per_unit", "units_sold"]

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
#%%

# Oppgave 4

#4a)
#) Create a bar plot to show the revenue (sum of sales) for each product.

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

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

# Plot for Macbook Air
ax[0, 0].hist(Macbook['sales_price_per_unit'], bins=10, color='lightblue', edgecolor='black')
ax[0, 0].set_title('Macbook Air')
ax[0, 0].set_xlabel('Sales Price')
ax[0, 0].set_ylabel('Frequency')

# Plot for Lenovo Thinkpad
ax[0, 1].hist(Lenovo['sales_price_per_unit'], bins=10, color='lightgreen', edgecolor='black')
ax[0, 1].set_title('Lenovo Thinkpad')
ax[0, 1].set_xlabel('Sales Price')
ax[0, 1].set_ylabel('Frequency')

# Plot for iPhone 14
ax[1, 0].hist(Iphone['sales_price_per_unit'], bins=10, color='lightcoral', edgecolor='black')
ax[1, 0].set_title('iPhone 14')
ax[1, 0].set_xlabel('Sales Price')
ax[1, 0].set_ylabel('Frequency')

# Plot for Samsung Galaxy S22
ax[1, 1].hist(Samsung['sales_price_per_unit'], bins=10, color='plum', edgecolor='black')
ax[1, 1].set_title('Samsung Galaxy S22')
ax[1, 1].set_xlabel('Sales Price')
ax[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# %%
#5 

#a)
import statsmodels.api as sm

# Liste med produktene
products = ['Macbook Air', 'Lenovo Thinkpad', 'Iphone 14', 'Samsung Galaxy S22']

# Loop gjennom hvert produkt
for product in products:
    print(f"\n🔹 Regression for {product}")
    
    # Filtrer for bare dette produktet
    df = result[result['product_name'] == product]
    
    # Definer X og Y
    X = df[['sales_price_per_unit']]
    Y = df['units_sold']
    
    # Legg til konstantledd (alpha)
    X = sm.add_constant(X)
    
    # Estimer regresjonsmodellen
    model = sm.OLS(Y, X).fit()
    
    # Skriv ut R-squared og koeffisienter
    print(model.summary())

#5b)

#If the products are priced by their average price. How much of the
#four products would Murloc Inc. sell, on average?
import pandas as pd
import statsmodels.api as sm

# 1. Beregn gjennomsnittspris for hvert produkt
avg_prices = result.groupby('product_name')['sales_price_per_unit'].mean()

# 2. Legg inn gjennomsnittspris i ny kolonne
result['avg_price'] = result['product_name'].map(avg_prices)

# 3. Lag tom liste for å samle resultater
prediction_list = []

# 4. Hent unike produkter
products = result['product_name'].unique()

# 5. Gå gjennom hvert produkt og estimer modell
for product in products:
    df = result[result['product_name'] == product]  # Filtrer
    X = df[['sales_price_per_unit']]
    Y = df['units_sold']
    
    X = sm.add_constant(X)  # Legg til konstantledd
    model = sm.OLS(Y, X).fit()

    # Bruk gjennomsnittspris for dette produktet til å lage prediksjon
    avg_price = avg_prices.loc[product]
    pred_input = pd.DataFrame({'const': [1], 'sales_price_per_unit': [avg_price]})
    pred_units = model.predict(pred_input)[0]

    # Legg til i liste
    prediction_list.append({
        'product_name': product,
        'avg_price': avg_price,
        'predicted_units_sold': pred_units
    })

# 6. Lag tabell
prediction_df = pd.DataFrame(prediction_list)

# 7. Vis tabellen
from IPython.display import display
display(prediction_df)

#c)

import pandas as pd
import statsmodels.api as sm

# 1. Beregn gjennomsnittspris for hvert produkt
avg_prices = result.groupby('product_name')['sales_price_per_unit'].mean()

# 2. Øk prisene med 10 %
increased_prices = avg_prices * 1.10

# 3. Legg til ny kolonne i result (valgfritt)
result['increased_price'] = result['product_name'].map(increased_prices)

# 4. Lag tom liste for resultater
prediction_list = []

# 5. Hent unike produkter
products = result['product_name'].unique()

# 6. Gå gjennom hvert produkt
for product in products:
    df = result[result['product_name'] == product]
    X = df[['sales_price_per_unit']]
    Y = df['units_sold']

    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()

    # Bruk 10% økt gjennomsnittspris
    increased_price = increased_prices.loc[product]
    pred_input = pd.DataFrame({'const': [1], 'sales_price_per_unit': [increased_price]})
    pred_units = model.predict(pred_input)[0]

    # Legg til resultat
    prediction_list.append({
        'product_name': product,
        'increased_price': increased_price,
        'predicted_units_sold': pred_units
    })

# 7. Lag tabell
prediction_df = pd.DataFrame(prediction_list)

# 8. Vis tabellen
from IPython.display import display
display(prediction_df)


#%%

#Oppgave 6

#6a
def oppgave_6(x, y):
    secure_password = generate_password()
    user_want_access = input("Please give me the password to open function:")
    
    while user_want_access != secure_password:
        print("Incorrect password, try again: ")
        user_want_access = input("Please give me the password to open function:")
    else:
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        return model.rsquared_adj

#6b

#Filtrerer for ett produkt
df_macbook = result[result['product_name']== 'Macbook Air']

#Definerer X og Y
x = df_macbook[['sales_price_per_unit']]
y = df_macbook['units_sold']

#kall på funksjon
adjusted_r2 = oppgave_6(x, y)

print(f"Adjusted R2 for Macbook Air: {adjusted_r2}")

# %%
