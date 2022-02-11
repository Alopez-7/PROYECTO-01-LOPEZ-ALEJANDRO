from hashlib import new
from lifestore_file import lifestore_products, lifestore_sales
from classes import ItemSales
from pprint import pprint



sales =  [ItemSales()]
sales.clear()
i=0
products_sales = {}
for product in lifestore_products:
    sales.append(ItemSales(product[1],product[0]))
    for productsale in lifestore_sales:
        if productsale[1] == sales[i].idProduct:
            sales[i].sales +=1
    i+=1

sortedBySales = sorted(sales, key=lambda x: x.sales,reverse=True)
 
pprint(sortedBySales)
