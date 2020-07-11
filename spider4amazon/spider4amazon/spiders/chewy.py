import scrapy
from bs4 import BeautifulSoup
import re
from scrapy import Request
# import spider4amazon.spider4amazon.items.AmazonItems

class demo(scrapy.Spider):
    name = "negg"
    allowed_domains =["www.newegg.ca"]

    start_urls =[
        "https://www.newegg.ca/p/pl?d=wifi+camera"
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, callback = self.parse, meta={'proxy', 'http://129.125.195.155:8888'})

    def parse(self, response):
        # items = []
        #
        filename = response.url.split("/")[-2]
        soup = BeautifulSoup(response.body, 'html.parser')
        containers = soup.find_all("div.item-inner")
        print(len(containers))



    # def parse_details(self,response):
    #     soup = BeautifulSoup(response.body,'html.parser')
    #     name = self.extract_name(soup)
    #     try:
    #         name = self.extract_name(soup)
    #         if name is None:
    #             raise Exception('Name not found ' + response.url)
    #     except Exception as e:
    #         self.logger.error(str(e))
    #
    #
    # def extract_name(self,soup):
    #     selectors = ["span#productTitle"]
    #     for selector in selectors:
    #         if len(soup.select(selector)) != 0:
    #             name = soup.select(selector)[0].txt
    #             print("-----------------")
    #             print(name)
    #             return name







