# -*- coding: utf-8 -*-
import scrapy


class Spyde1Spider(scrapy.Spider):
    name = 'spyde1'
    allowed_domains =[]
    url = "www.jumia.co.ke/"
    categories = ['women-s-fashion/','women-accessorie/','bags-accessories/',
                  'womens-trousers-leggings/','womens-tops/','women-s-clothing/','women-s-shoes/',
                  'womens-dresses/','womens-skirts/','heels/','lingerie-sleepwear/']
    for category in categories:
        domain = url+category
        allowed_domains.append(domain)

    start_urls = ['http://'+ domain for domain in allowed_domains]
    # start_urls = ['http://www.jumia.co.ke/women-s-fashion/']

    #location of csv file
    custom_settings = {
        'FEED_URI' : 'tmp/scrapped_data/images/jumia.csv'
    }

    def parse(self, response):
        #Extracting the content using css selectors
        images = response.css("img.lazy.image::attr(data-src)").extract()
        titles = response.css("img::attr(alt)").extract()
        prices = response.css("span::attr(data-price)").extract()

        for item in zip(titles,prices,images):
            scraped_info = {
            'title' : item[0],
            'price' : item[1],
            'image_urls' : [item[2]] #Set's the url for scrapy to download images

            }

            yield scraped_info
