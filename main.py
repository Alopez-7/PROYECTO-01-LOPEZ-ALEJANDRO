from ast import While
from audioop import avg
from functools import total_ordering
from hashlib import new
from math import floor, prod
from typing import List
from unicodedata import category
from lifestore_file import lifestore_products, lifestore_sales,lifestore_searches
from classes import ItemSales, TopSearches,ItemReviews,ProductSales,ProductSalesDate
from pprint import pprint
from datetime import datetime
from calendar import monthrange

dictMonths={
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
    }
def logIn():
    print("<<<<<<<<<Bienvenido>>>>>>>>>")
    i=0
    while True:
        if i == 3:
            print ("Usuario incorrecto" , "SISTEMA BLOQUEADO")
            exit()
        print("-------------------------")
        print("Iniciar Sesion")
        username = input("Username:")
        if username == "SuperUser" :
            print ("Escriba Contraseña")
            break

        else :
            i+=1
            print (f'Nombre de usuario incorrecto. quedan {3-i} intentos')
    i=0
    while True:
        if i == 3:
            print ("Contraseña incorrecta" , "SISTEMA BLOQUEADO")
            exit()
        password = input ("Password:")
        if password  == "admin" :
            print ("ACCESO CONCEDIDO")
            print (f'<<Bienvnido {username} >>')
            break
     #continue for thins like opening webpages or hidden files for access

        else :
            print ("Contraseña incorrecta", "Intente de nuevo")
            i+=1
            print (f'Nombre de usuario incorrecto. quedan {3-i} intentos')
           

logIn()


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







def getTopSearches(productSearches:List[TopSearches],qty:int=10):
    """Funcion para obeter productos mas buscados"""
    sortedBySearches = sorted(productSearches,key=lambda x:x.searches, reverse=True)
    topSearches = sortedBySearches[0:qty]
    print("------------------------------------------------------------------------------------------------------------------------") 
    print("Productos Mas Buscados")
    for items in topSearches:
         print(f'\t  Nombre: {items.productName} ID: {items.idProduct} Ventas: {items.searches} ')


def getTopSales(productSales:List[ItemSales],qty:int=5):
    """Funcion para obetener productos mas vendidos"""
    sortedBySales = sorted(productSales, key=lambda x: x.sales,reverse=True)
    topSales = sortedBySales[0:qty]
    print("------------------------------------------------------------------------------------------------------------------------")
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


def worstProductsByCat(products:dict,qty:int=10):
    """Funcion para obtener y ordener los 5 productos menos vendidos por categoria"""
    catSales = {}
    
   
    
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
        print("------------------------------------------------------------------------------------------------------------------------")
        print(f'Categoria {key} Menos Vendidos:')
        pprint(lSales[key])
           
   # pprint(lSales)

def worstProductSearchesByCat(products:dict,qty:int=10):
    """Funcion para obtener y ordener los productos menos vendidos por categoria"""
    catSearches = {}
   
    
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
        print("------------------------------------------------------------------------------------------------------------------------")
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
    print("------------------------------------------------------------------------------------------------------------------------")
    print("MEJOR CALIFICADOS:")
    for key,value in topRatedList.items():
        print(f'Producto: {key} Calificacion: {value}')
    print("------------------------------------------------------------------------------------------------------------------------")    
    print("PEOR CALIFICADOS:")
    for key,value in worstProductList.items():
        print(f'Producto: {key} Calificacion: {value}')
    return(reviewAvg)    
     

   

listOfSales = [ProductSales()]
listOfSales.clear()

for sale in lifestore_sales:
    listOfSales.append(ProductSales(idProduct=sale[1],date=sale[3],
    day=sale[3][0:2],month=sale[3][3:5],year=sale[3][6:10],returned=bool(sale[4])))



for product in lifestore_products:
    i=0
    for sale in listOfSales:
        if product[0] == sale.idProduct:
            listOfSales[i].price=product[2]
            listOfSales[i].productName=product[1]
        i+=1    
    
def anualProfit():
    print("------------------------------------------------------------------------------------------------------------------------")
    totalEarnings=0
    for sale in listOfSales:
        if not sale.returned:
            totalEarnings += sale.price
    print(f'Ganancia anual: ${totalEarnings}')
    print("------------------------------------------------------------------------------------------------------------------------")
    print(f'Ganancia promedio Mensual: ${totalEarnings/12}')

def monthlySales():
    
    mSales={}
    mSalesCash={}
    print("------------------------------------------------------------------------------------------------------------------------")
    for month in range(1,13):
        mSales[dictMonths[month]]=0
        mSalesCash[dictMonths[month]]=0
        for sale in listOfSales:
            if int(sale.month)==month:
                
                mSales[dictMonths[month]]+=1
                mSalesCash[dictMonths[month]]+=sale.price
    print("VENTAS PROMEDIO POR MES")
    avgSM=0
    for value in mSales.values():
        avgSM+=value
    
    print(f'{floor(avgSM/12.)} ventas')
    print("------------------------------------------------------------------------------------------------------------------------")
    print("VENTAS POR MES")
    sort_orders = sorted(mSales.items(), key=lambda x: x[1], reverse=True)
 
    for value in sort_orders:
        print(f'Mes: {value[0]} Ventas: {value[1]}')
    print("------------------------------------------------------------------------------------------------------------------------")
    print("GANANCIAS POR MES")
    sort_orders2 = sorted(mSalesCash.items(), key=lambda x: x[1], reverse=True)
 
    for value in sort_orders2:
        print(f'Mes: {value[0]} Ventas: ${value[1]}')
        

  
            
            


print("GENERANDO REPORTE")

getTopSales(sales)

getTopSearches(searches)

worstProductsByCat(makeCategoriesList(sales))

worstProductSearchesByCat(makeCategoriesList(sales))

scoreAvg()
anualProfit()
monthlySales()



