from bs4 import BeautifulSoup
from typing import List
import urllib.parse
import urllib.request
import re
import ssl
from services import service_scraping
from services import service_DB
from fastapi import HTTPException


def set_quantities(list_ingredient, nb_old, nb_pers):
    counts = [ingredient["quantity"] for ingredient in list_ingredient]
    names = [ingredient["name"] for ingredient in list_ingredient]
    units = [ingredient["unit"] for ingredient in list_ingredient]
    if int(nb_old) != nb_pers:
        for i in range(len(counts)):
            qu = counts[i]
            if qu == "":
                continue
            qu = float(qu)
            counts[i] = qu * nb_pers / int(nb_old)
        new_list = [
            {"name": n, "quantity": c, "unit": u}
            for (n, c, u) in zip(names, counts, units)
        ]
        return new_list
    return list_ingredient


def aggregate(ingredient, unit, count):
    ingredients = []
    for i in range(len(ingredient)):
        ingredients.append([ingredient[i], unit[i], count[i]])
    return ingredients


def merge_two(list1, list2):
    res = []
    done = []
    for ingredients in list1:
        ingredient = ingredients["name"]
        count = ingredients["quantity"]
        unit = ingredients["unit"]
        l = len(done)
        for i in range(len(list2)):
            if (ingredient == list2[i]["name"]) and (unit == list2[i]["unit"]):
                if count == "":
                    done.append(i)
                    res.append(list2[i])
                elif list2[i]["quantity"] == "":
                    done.append(i)
                    res.append({"name": ingredient, "quantity": count, "unit": unit})
                else:
                    done.append(i)
                    res.append(
                        {
                            "name": ingredient,
                            "quantity": float(count) + float(list2[i]["quantity"]),
                            "unit": unit,
                        }
                    )
        if len(done) == l:
            res.append({"name": ingredient, "quantity": count, "unit": unit})

    for i in range(len(list2)):
        if i not in done:
            res.append(list2[i])

    return res


async def get_shopping_list(strings, nb_pers):
    recipes = []
    for string in strings:
        try:
            recipe = await service_DB.read_recipe(string)
            print("I have {} in the database".format(string))
        except HTTPException:
            recipe = service_scraping.get_recipe_from_scrap(string)
            print("Never heard of {}, scrapped it and got {}".format(string, recipe))
            _ = await service_DB.create_recipe(recipe)
        recipes.append(recipe)

    ingredients_lists = []
    for recipe in recipes:
        # print(recipe)
        ingredients_lists.append(
            set_quantities(recipe["ingredients"], recipe["nb_persons"], nb_pers)
        )

    first = ingredients_lists[0]
    for i in range(1, len(ingredients_lists)):
        first = merge_two(first, ingredients_lists[i])

    return first
