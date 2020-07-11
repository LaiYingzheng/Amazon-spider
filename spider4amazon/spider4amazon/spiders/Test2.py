import scrapy
from bs4 import BeautifulSoup
import re
from scrapy import Request
import pandas as pd


class test(scrapy.Spider):
    name = "demo"
    allowed_domains = "www.amazon.ca"

    def get_all_url(num_page):
        urls = []
        i = 0
        while i < num_page:
            urls.append(
                "https://www.amazon.ca/s?k=wifi+camera&page=" + str(i + 1) + "&qid=1593842684&ref=sr_pg_" + str(i))
            i += 1
        return urls

    start_urls = get_all_url(1)




    result = pd.DataFrame({
        'Product name':[],
        'Product price': [],
        'Product description': [],
        'Product shipping': [],
        'Product details': [],
        'Product review': [],
        'Product rating': [],


    })
    #
    # PROXY = "http://51.79.161.3:8080"
    #
    # def start_requests(self):
    #     for url in self.start_urls:
    #         request = Request(url, callback = self.parse)
    #         request.meta['proxy'] = self.PROXY
    #         yield request

    def parse(self, response):

        soup = BeautifulSoup(response.body, 'html.parser')

        tags = soup.findAll('a', href=re.compile("dchild=1#customerReviews"))
        i = 0
        for tag in tags:
            if i < 1:
                url = "https://amazon.ca" + tag.get('href')
                i += 1
                yield scrapy.Request(url, callback=self.parse_details, dont_filter=True)

    def parse_details(self,response):
        soup = BeautifulSoup(response.body, 'html.parser')
        name = self.e_name(soup)
        shipping = self.e_shipping(soup)
        descr = self.e_Desc(soup)
        info = self.e_details(soup)
        price = self.e_price(soup)
        review = self.e_review(soup)
        rating = self.e_rating(soup)

        self.result =self.result.append(pd.DataFrame({
            'Product name': [name],
            'Product price': [price],
            'Product description': [descr],
            'Product shipping': [shipping],
            'Product details': [info],
            'Product review': [review],
            'Product rating': [rating],
        }))

        print(self.result)
        # self.result.to_csv(r'/Users/lait/PycharmProjects/spider/spider4amazon/spider4amazon/spiders/demo.csv',index = False, header = True)
    def e_details(self,soup):

        selectors = [
            'div#feature-bullets',
            'div#feature-bulflets',
        ]

        info = []
        for selector in selectors:
            details = soup.select(selector)
            if len(details)==0:
                info.append("Information Not Found")
            else:
                for detail in details:
                    info.append(detail.text)

        return info

    def e_name(self, soup):

        selectors = [
            'span#productTitle',
        ]

        name = []
        for selector in selectors:
            details = soup.select(selector)
            if len(details) == 0:
                details.append("Information Not Found")
            else:
                for detail in details:
                    name.append(detail.text.replace("\n\n\n\n\n\n\n\n",""))

        return name

    def e_price(self, soup):
        selectors = [
            'span#priceblock_ourprice',
            'span#priceblock_saleprice'
        ]

        price = []
        for selector in selectors:

            details = soup.select(selector)
            if len(details) == 0:
                price.append("Information Not Found")
            else:
                 for detail in details:
                    price.append(detail.text)

        return price

    def e_shipping(self, soup):
        selectors = [
            'span#price-shipping-message',
        ]

        shipping = []
        for selector in selectors:

            details = soup.select(selector)
            if len(details) == 0:
                shipping.append("Information Not Found")
            else:
                for detail in details:
                    shipping.append(detail.text)

        return shipping

    def e_Desc(self, soup):

        selectors = [
            'div#productDescription'
        ]

        desc = []
        for selector in selectors:
            details = soup.select(selector)
            if len(details) == 0:
                desc.append("Information Not Found")
            else:
                for detail in details:
                    desc.append(detail.text)

        return desc

    def e_review(self,soup):

        selectors = [
            'span#acrCustomerReviewText',
        ]

        review = []
        for selector in selectors:
            details = soup.select(selector)
            if len(details)==0:
                review.append("Information Not Found")
            else:
                for detail in details:
                    review.append(detail.text.replace('ratings',"").replace(" ",""))

        return review



    def e_rating(self,soup):

        selectors = [
            'div#averageCustomerReviews',
        ]

        rating = []
        for selector in selectors:
            details = soup.select(selector)
            if len(details)==0:
                rating.append("Information Not Found")
            else:
                for detail in details:
                    rating.append(detail.text.replace("\n\n\n\n\n","")[:3])

        return rating
