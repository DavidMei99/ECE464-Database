# Di Mei
# ECE464 pset#2: Web Scraper
# reference: https://realpython.com/web-scraping-with-scrapy-and-mongodb/
# create a Spider

from scrapy import Spider
from scrapy.selector import Selector
from recipe.items import RecipeItem

class RecipeSpider(Spider):
    name = "recipe"
    allowed_domains = ["https://www.delish.com"]
    start_urls = ["https://www.delish.com/weeknight-dinners/"]

    def parse(self, response):
        recipes = Selector(response).xpath('//div[@class="full-item-content"]') 
        for recipe in recipes:
            item = RecipeItem()
            item['recipe_title'] = recipe.xpath(
                'a[@class="full-item-title item-title"]/text()').extract()[0]
            item['recipe_url'] = recipe.xpath(
                'a[@class="full-item-title item-title"]/@href').extract()[0]
            author = recipe.xpath(
                'div[@class="byline "]/span/text()').re('[^\t\n]+')
            if author:
                item['recipe_author'] = author[0]
            else:
                item['recipe_author'] = 'None'
            yield item
