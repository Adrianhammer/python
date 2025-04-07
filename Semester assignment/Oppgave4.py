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
