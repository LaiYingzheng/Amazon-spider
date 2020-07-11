 # Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider4AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AmazonItems(scrapy.Item):
    name = scrapy.Field() # Product Name
    price = scrapy.Field() # Product Price
    rating = scrapy.Field() #Product rating
    Shipping = scrapy.Field() #Product Shipping price

