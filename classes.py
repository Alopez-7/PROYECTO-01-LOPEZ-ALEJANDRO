from dataclasses import dataclass
from itertools import product
from mimetypes import init
from pickle import EMPTY_LIST
from queue import Empty
from typing import List
from unicodedata import category

@dataclass
class ItemSales:
    
    """Class for keeping track of an item in inventory."""
    productName: str =''
    idProduct: str =""
    category:str =""
    sales: int=0


@dataclass
class TopSearches:
    productName: str =''
    idProduct: str =""
    searches: int=0


  