from hashlib import new
from math import prod
from typing import List
from unicodedata import category
from lifestore_file import lifestore_products, lifestore_sales,lifestore_searches
from classes import ItemSales, TopSearches
from pprint import pprint


#Generar e instanciar dataclass contenedora de lista lifestore_products
sales =  [ItemSales()]
sales.clear()
i=0
for product in lifestore_products:
    sales.append(ItemSales(product[1],product[0],product[3]))
    for productsale in lifestore_sales:
        if productsale[1] == sales[i].idProduct:
            sales[i].sales +=1
    i+=1

#Generar e instanciar dataclass contenedora de lista lifestore_searches
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
    """Funcion para obeter productos mas buscados"""
    sortedBySearches = sorted(productSearches,key=lambda x:x.searches, reverse=True)
    topSearches = sortedBySearches[0:qty]
    print("Productos Mas Buscados")
    for items in topSearches:
         print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.searches} ')


def getTopSales(qty:int,productSales:List[ItemSales]):
    """Funcion para obetener productos mas vendidos"""
    sortedBySales = sorted(productSales, key=lambda x: x.sales,reverse=True)
    topSales = sortedBySales[0:qty]
    print("Productos Mas Vendidos")
    for items in topSales:
        print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.sales} ')







def makeCategoriesList(productSales:List[ItemSales]):
    """Funcion para obtener el listado de categorias"""
    prodCategories = {}
    for item in productSales:
        if item.category not in prodCategories.keys():
           prodCategories[item.category]=[]
        prodCategories[item.category].append(item.idProduct)
    return prodCategories


def bestProductsByCat(products:dict):
    """Funcion para obtener y ordener los 5 productos menos vendidos por categoria"""
    catSales = {}
    print("")
    
    for cat in products.keys():
        n=0
        catSales[cat]=[]

        for item in sales:
            if sales[n].category == cat:
                catSales[cat].append(sales[n])
            n+=1
    lSales={}
    for item in catSales.keys():
        lSales[item] =[]
        sortedList= sorted(catSales[item],key=lambda x:x.sales)
        lSales[item].append(sortedList[0:5])
        
    for key in lSales.keys():
        print(f'Categoria {key} Menos Vendidos:')
        pprint(lSales[key])
           
   # pprint(lSales)
     
     
print("GENERANDO REPORTE")
getTopSales(5,sales)
getTopSearches(10,searches)
bestProductsByCat(makeCategoriesList(sales))