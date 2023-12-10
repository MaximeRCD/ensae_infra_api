from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re
import ssl
import service_scraping
import service_DB

def aggregate(ingredient,unit,count):
    ingredients = []
    for i in range(len(ingredient)):
        ingredients.append([ingredient[i],unit[i],count[i]])
    return ingredients

def merge_two(list1, list2):
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
@staticmethod

def _get_shopping_list(strings,list_nb):

    recipes = []
    for string in strings:
        if service_DB.is_string_in_DB(string):  
            recipe = service_DB.get_recipe_from_DB(string)  
            recipes.append(recipe)
        else:
            recipe = service_scraping.get_recipe_from_scrap(string)   
            recipe.append(recipe)
    
    ingredients_lists = [recipe.ingredients for recipe in recipes]
    
    first=ingredients_lists[0]
    for i in range(1,len(res)):
        first=merge_two(first,ingredients_lists[i])
    return first



'''for (url,nb) in zip(urls,list_nb):
    soup = get_soup_from_url(url)
    ingredients_lists.append(_get_ingredients(soup))
    count_lists.append(set_quantities(soup,_get_quantities(soup),nb))
    units_lists.append(_get_units(soup))
for (ingredient,count,unit) in zip(ingredients_lists,count_lists,units_lists):
    res.append((aggregate(ingredient,count,unit)))
first=res[0]
for i in range(1,len(res)):
    first=merge_two(first,res[i])
return first'''