# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Di Mei
# ECE464 pset#2: Web Scraper
# reference: https://realpython.com/web-scraping-with-scrapy-and-mongodb/
# define storage "containers" for the scraped data

import scrapy
from scrapy.item import Item, Field 

class RecipeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    recipe_title = Field()
    recipe_url = Field()
    recipe_author = Field()
    pass
