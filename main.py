from hashlib import new
from math import prod
from typing import List
from unicodedata import category
from lifestore_file import lifestore_products, lifestore_sales,lifestore_searches
from classes import ItemSales, TopSearches
from pprint import pprint



sales =  [ItemSales()]
sales.clear()
i=0
for product in lifestore_products:
    sales.append(ItemSales(product[1],product[0],product[3]))
    for productsale in lifestore_sales:
        if productsale[1] == sales[i].idProduct:
            sales[i].sales +=1
    i+=1

searches = [TopSearches()]
searches.clear()

i=0
for items in sales:
    searches.append(TopSearches(items.productName,items.idProduct))
    for searchesItem in lifestore_searches:
        if searchesItem[1] == searches[i].idProduct:
            searches[i].searches += 1
    i +=1

 
def getTopSearches(qty:int,productSearches:List[TopSearches]):
    sortedBySearches = sorted(productSearches,key=lambda x:x.searches, reverse=True)
    topSearches = sortedBySearches[0:qty]
    for items in topSearches:
         print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.searches} ')


def getTopSales(qty:int,productSales:List[ItemSales]):
    sortedBySales = sorted(productSales, key=lambda x: x.sales,reverse=True)
    topSales = sortedBySales[0:qty]
    for items in topSales:
        print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.sales} ')
#getTopSales(5,sales)



#prodCategories['test'] = sales[0].productName


def makeCategoriesList(productSales:List[ItemSales]):
    prodCategories = {}
    for item in productSales:
        if item.category not in prodCategories.keys():
           prodCategories[item.category]=[]
        prodCategories[item.category].append(item.idProduct)
    return prodCategories


        
def bestProductsByCat(products:dict):
    for cat in products.keys():
        for itemSales in sales:
            ##if cat in itemSales
                
                print()


bestProductsByCat(makeCategoriesList(sales))
