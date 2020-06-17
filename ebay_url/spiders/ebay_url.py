import scrapy

from scrapy.spiders import CrawlSpider

class EbayUrlSpider(CrawlSpider):

    #
    name = 'ebay_url'

    #
    allowed_domains = ['ebay.com']

    #
    start_urls = ['https://www.ebay.com']

    #
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    def parse_httpresponse():
        
        return