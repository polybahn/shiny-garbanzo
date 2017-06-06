# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from lauchforth.items import LauchforthItem


class LauchforthCrawlerSpider(CrawlSpider):
    name = 'lauchforth_crawler'
    allowed_domains = ['launchforth.io']
    start_urls = ['https://launchforth.io/api/v2/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = LauchforthItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
