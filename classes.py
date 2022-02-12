from dataclasses import dataclass
from itertools import product
from mimetypes import init
from pickle import EMPTY_LIST
from queue import Empty
from typing import List
from unicodedata import category

@dataclass
class ItemSales:
    
    """Objeto para contener informacion de los productos."""
    productName: str =''
    idProduct: str =""
    category:str =""
    sales: int=0
    

    


@dataclass
class TopSearches:
    """Objeto para contener informacion de busquedas de los productos."""
    productName: str =''
    idProduct: str =""
    searches: int=0
    category: str =""


@dataclass
class ItemReviews:
    
    """Objeto para contener informacion de los productos."""
    productName: str =''
    idProduct: str =""
    score: int=0

@dataclass
class ProductSales:
    productName: str =''
    idProduct: str =""
    date: str=""
    price:int = 0