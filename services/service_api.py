from bs4 import BeautifulSoup
from typing import List
import urllib.parse
import urllib.request
import re
import ssl
import service_scraping
import service_DB


async def set_quantities(list_ingredient,nb_old,nb_pers):
    counts=[ingredient['quantity'] for ingredient in list_ingredient]
    names=[ingredient['name'] for ingredient in list_ingredient]
    units=[ingredient['unit'] for ingredient in list_ingredient]
    if int(nb_old) != nb_pers:
        for i in range(len(counts)):
            qu = counts[i]
            qu=float(qu)
            counts[i] = qu* nb_pers/int(nb_old)
        new_list=[{'name':n,'quantity':c,'unit':u} for (n,c,u) in zip(names,counts,units)]
        return new_list
    return list_ingredient


async def aggregate(ingredient,unit,count):
    ingredients = []
    for i in range(len(ingredient)):
        ingredients.append([ingredient[i],unit[i],count[i]])
    return ingredients

async def merge_two(list1, list2):
    res=[]
    done=[]
    for ingredient,count,unit in list1:
        l=len(done)
        for i in range(len(list2)):
            if (ingredient == list2[i][0]) and (unit == list2[i][2]) :
                done.append(i)
                res.append([ingredient,float(count)+float(list2[i][1]),unit])
        if len(done)==l:
            res.append([ingredient,count,unit])
                
    for i in range(len(list2)):
        if i not in done:
            res.append(list2[i])
        
    return res

async def get_shopping_list(strings:List(str),nb_pers:int):
    recipes = []
    for string in strings:  
        if service_DB.is_string_in_DB(string):  
            recipe = service_DB.get_recipe_from_DB(string)  
            recipes.append(recipe)
        else:
            recipe = service_scraping.get_recipe_from_scrap(string)   
            recipe.append(recipe)
    
    ingredients_lists = []
    for recipe in recipes:
        ingredients_lists.append(set_quantities(recipe.ingredients,recipe.nb_persons,nb_pers))
    
    first=ingredients_lists[0]
    for i in range(1,len(ingredients_lists)):
        first=merge_two(first,ingredients_lists[i])
        
    return first 

