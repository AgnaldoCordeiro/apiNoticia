# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApinoticiaItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    subtitulo = scrapy.Field()
    url = scrapy.Field()
    data = scrapy.Field()
    image_url = scrapy.Field()
    
