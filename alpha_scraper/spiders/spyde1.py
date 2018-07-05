# -*- coding: utf-8 -*-
import scrapy


class Spyde1Spider(scrapy.Spider):
    name = 'spyde1'
    allowed_domains = ['www.jumia.co.ke/women-s-fashion']
    start_urls = ['http://www.jumia.co.ke/women-s-fashion/']

    def parse(self, response):
        pass
