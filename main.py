from hashlib import new
from math import prod
from typing import List
from unicodedata import category
from lifestore_file import lifestore_products, lifestore_sales,lifestore_searches
from classes import ItemSales, TopSearches,ItemReviews,ProductSales
from pprint import pprint
from datetime import datetime

#Generar e instanciar dataclass ItemSales contenedora de lista lifestore_products
sales =  [ItemSales()]
sales.clear()
i=0
for product in lifestore_products:
    sales.append(ItemSales(product[1],product[0],product[3]))
    for productsale in lifestore_sales:
        if productsale[1] == sales[i].idProduct:
            sales[i].sales +=1
    i+=1

#Generar e instanciar dataclass TopSearches contenedora de lista lifestore_searches
searches = [TopSearches()]
searches.clear()

i=0
for items in sales:
    searches.append(TopSearches(items.productName,items.idProduct,category=items.category))
    for searchesItem in lifestore_searches:
        if searchesItem[1] == searches[i].idProduct:
            searches[i].searches += 1
    i +=1

#Generar e instanciar dataclass Reviews contenedora de lista lifestore_searches

reviews = [ItemReviews()]
reviews.clear()
i=0
for items in lifestore_sales:
    reviews.append(ItemReviews(idProduct=items[1],score=items[2]))
for reviewt in reviews:
    for sale in sales:
        if reviewt.idProduct == sale.idProduct:
            reviews[i].productName = sale.productName
    i+=1







def getTopSearches(productSearches:List[TopSearches],qty:int=5):
    """Funcion para obeter productos mas buscados"""
    sortedBySearches = sorted(productSearches,key=lambda x:x.searches, reverse=True)
    topSearches = sortedBySearches[0:qty]
    print("Productos Mas Buscados")
    for items in topSearches:
         print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.searches} ')


def getTopSales(productSales:List[ItemSales],qty:int=5):
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


def worstProductsByCat(products:dict,qty:int=5):
    """Funcion para obtener y ordener los 5 productos menos vendidos por categoria"""
    catSales = {}
    print("IMPRIMIENDO PRODCUTOS MENOS VENDIDOS")
    
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
        lSales[item].append(sortedList[0:qty])
        
    for key in lSales.keys():
        print(f'Categoria {key} Menos Vendidos:')
        pprint(lSales[key])
           
   # pprint(lSales)

def worstProductSearchesByCat(products:dict,qty:int=10):
    """Funcion para obtener y ordener los productos menos vendidos por categoria"""
    catSearches = {}
    print("IMPRIMIENDO PRODCUTOS MENOS BUSCADOS")
    
    for cat in products.keys():
        n=0
        catSearches[cat]=[]

        for item in searches:
            if searches[n].category == cat:
                catSearches[cat].append(searches[n])
            n+=1
    lSearches={}
    for item in catSearches.keys():
        lSearches[item] =[]
        sortedList= sorted(catSearches[item],key=lambda x:x.searches)
        lSearches[item].append(sortedList[0:qty])
        
    for key in lSearches.keys():
        print(f'Categoria {key} Menos Buscados:')
        pprint(lSearches[key])

def scoreAvg():
  
    reviewAvg={}

    for review in reviews:
        if review.idProduct not in reviewAvg.keys():
            reviewAvg[review.productName]=[]
    for key in reviewAvg.keys():
        scoreSum = 0
        elements=0
        for item in reviews:
            if item.productName == key:
                scoreSum+=item.score
                elements+=1
        reviewAvg[key]=scoreSum/elements
    topRatedList={}
    worstProductList={}
    for key,value in reviewAvg.items():
        if value >= 4:
            topRatedList[key] = value
        else:
            worstProductList[key] = value

    print("Mejor Calificados:")
    for key,value in topRatedList.items():
        print(f'Producto: {key} Calificacion: {value}')
    print("Peor Calificados:")
    for key,value in worstProductList.items():
        print(f'Producto: {key} Calificacion: {value}')
    return(reviewAvg)    
     

   

listOfSales = [ProductSales()]
listOfSales.clear()

for sale in lifestore_sales:
    listOfSales.append(ProductSales(idProduct=sale[1],date=sale[3]))

i=0

for sale in listOfSales:
    if sale.idProduct == lifestore_products[i][0]:
        print("TEEST")
    i+=1    
    
print(lifestore_products[0][2])

print("GENERANDO REPORTE")
getTopSales(sales)
getTopSearches(searches)
worstProductsByCat(makeCategoriesList(sales))
worstProductSearchesByCat(makeCategoriesList(sales))
scoreAvg()
