from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re
import ssl

#returns soup of first result recipe from a query

def get_url_from_query(query_dict):
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
    return url

def get_url_from_string(string):

    query_dict = {'aqt': string}

    return get_url_from_query(query_dict)

def get_soup_from_url(url):


    try:
        handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        opener = urllib.request.build_opener(handler)
        response = opener.open(url)
        html_content = response.read()
    except urllib.error.HTTPError as e:
        raise RecipeNotFound if e.code == 404 else e

    soup = BeautifulSoup(html_content, 'html.parser')

    return soup

def _get_name(soup):
	return soup.find("h1").get_text().strip(' \t\n\r')


def _get_ingredients(soup):
      ingredients = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "ingredient-name"})]
      return ingredients

def _get_quantities(soup):
    count = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "count"})]
    return count


def _get_units(soup):
    units = [i.get_text().strip(' \t\n\r') for i in soup.findAll("span", {"class": "unit"})]
    return units

def _get_nb_persons(soup):
    input_element = soup.find("div", {"class": "mrtn-recette_ingredients-counter"})
    nb = input_element.get('data-servingsnb')
    #print('(pour ' + nb + ' personnes)')
    return nb    

def set_quantities(soup,count,nb_pers):
    nb = _get_nb_persons(soup)
    if int(nb) != nb_pers:
        for i in range(len(count)):
            qu = count[i]
            qu=float(qu)
            count[i] = qu* nb_pers/int(nb)
    return count

def aggregate(ingredient,unit,count):
    ingredients = []
    for i in range(len(ingredient)):
        ingredients.append([ingredient[i],unit[i],count[i]])
    return ingredients

### importer model recipe
def _get_recipe_from_scrap(string):  ### refaire le return 
    url = get_url_from_string(string)
    soup = get_soup_from_url(url)
    name = _get_name(soup)
    ingredients = _get_ingredients(soup)
    count = _get_quantities(soup)
    unit = _get_units(soup)
    nb_persons = _get_nb_persons(soup)
    ingredients = aggregate(ingredients,unit,count)
    recipe={"name": name, "url": url, "ingredients": ingredients, "nb_persons": nb_persons}
    return recipe

#print(_get_recipe_from_scrap("poulet")) pour tester