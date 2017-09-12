import scrapy
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from myproject.items import Product

class raptorsSpider(scrapy.Spider):
    name = 'raptorsSpider'
    start_urls = ['https://staging.raptorsupplies.com/picnic-bench-850542',
 ]

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//*[@id="spec_attributes"]/div[1]/div[2]')
    return l.load_item()

