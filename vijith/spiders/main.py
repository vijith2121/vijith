import scrapy
# from vijith.items import Product
from lxml import html

class VijithSpider(scrapy.Spider):
    name = "vijith"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
