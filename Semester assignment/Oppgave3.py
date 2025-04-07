

import matplotlib.pyplot as plt
import pandas as pd

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
