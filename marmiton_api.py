# -*- coding: utf-8 -*-
#%%
from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re
import ssl
#%%
#%%
"""
Search recipes parsing the returned html data.
Options:
'aqt': string of keywords separated by a white space  (query search)
Optional options :
'dt': "entree" | "platprincipal" | "accompagnement" | "amusegueule" | "sauce"  (plate type)
'exp': 1 | 2 | 3  (plate expense 1: cheap, 3: expensive)
'dif': 1 | 2 | 3 | 4  (recipe difficultie 1: easy, 4: advanced)
'veg': 0 | 1  (vegetarien only: 1)
'rct': 0 | 1  (without cook: 1)
'sort': "markdesc" (rate) | "popularitydesc" (popularity) | "" (empty for relevance)
"""
query_dict = {
  "aqt": "fondue savoyarde",      # Query keywords - separated by a white space
  "dt": "platprincipal",      # Plate type : "entree", "platprincipal", "accompagnement", "amusegueule", "sauce" (optional)
  "exp": 2,                   # Plate price : 1 -> Cheap, 2 -> Medium, 3 -> Kind of expensive (optional)
  "dif": 2,                   # Recipe difficulty : 1 -> Very easy, 2 -> Easy, 3 -> Medium, 4 -> Advanced (optional)
  "veg": 0, 
  "": 0,                  # Vegetarien only : 0 -> False, 1 -> True (optional)
}

#returns soup of first result recipe from a query
def get_soup_from_query(query_dict):
    base_url = "http://www.marmiton.org/recettes/recherche.aspx?"
    query_url = urllib.parse.urlencode(query_dict)

    url = base_url + query_url

    handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    html_content = response.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    search_data = []

    articles = soup.findAll("a", href=True)
    articles = [a for a in articles if a["href"].startswith("/recettes/recette_")]  
    fichier = articles[0]

    iterarticles = iter(articles)
    for article in iterarticles:
        data = {}
        try:
            data["name"] = article.find("h4").get_text().strip(' \t\n\r')
            data["url"] = article['href']
            try:
                data["rate"] = article.find("span").get_text().split("/")[0]
            except Exception as e0:
                pass
            try:
                data["image"] = article.find('img')['data-src']
            except Exception as e1:
                try:
                    data["image"] = article.find('img')['src']
                except Exception as e1:
                    pass
                pass
        except Exception as e2:
            pass
        if data:
            search_data.append(data)
        
    uri = search_data[0]['url']
    base_url = "http://www.marmiton.org"
    url = base_url + ("" if uri.startswith("/") else "/") + uri

    try:
        handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        opener = urllib.request.build_opener(handler)
        response = opener.open(url)
        html_content = response.read()
    except urllib.error.HTTPError as e:
        raise RecipeNotFound if e.code == 404 else e

    soup = BeautifulSoup(html_content, 'html.parser')

    return soup



#%%
@staticmethod
def _get_name(soup):
	return soup.find("h1").get_text().strip(' \t\n\r')

@staticmethod
def _get_ingredients(soup):
      ingredients = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "ingredient-name"})]
      return ingredients
@staticmethod
def _get_quantities(soup):
    count = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "count"})]
    return count

@staticmethod
def _get_units(soup):
    units = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "unit"})]
    return units

def _get_nb_persons(soup):
    input_element = soup.find("div", {"class": "mrtn-recette_ingredients-counter"})
    nb = input_element.get('data-servingsnb')
    #print('(pour ' + nb + ' personnes)')
    return nb    
     
#%%
@staticmethod
def _get_shopping_list(queries):
	ingredients_lists = []
	count_lists=[]
	units_lists=[]
	for query_dict in queries:
		soup = get_soup_from_query(query_dict)
		ingredients_lists.append(_get_ingredients(soup))
		count_lists.append(_get_quantities(soup))
		units_lists.append(_get_units(soup))
	return ingredients_lists,count_lists,units_lists
          
# %%
