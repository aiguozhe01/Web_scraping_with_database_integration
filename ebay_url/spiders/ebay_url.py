import scrapy

from ebay_url.items import EbayUrlItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class EbayUrlSpider(CrawlSpider):

    # This name is required. It is how we refer to this PdfUrlSpider class on the command line.
    name = 'ebay_url'

    # Every link we look at MUST be a part of the adobe.com domain (i.e. contain "adobe.com" in it's url)
    allowed_domains = ['ebay.com']

    # This is the url we will start from (Check all the links on this webpage first, then go deeper)
    start_urls = ['https://www.ebay.com']

    # This Rule says:
    # 1. allow all links to be extracted
    # 2. call parse_httpresponse on each extracted link
    # 3. follow all links ("click" on them) so we can check all the links on THAT webpage too
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse', follow=True)]

    def parse_httpresponse(self, response):

        print(response.url)

        item = EbayUrlItem()

        # Check if the link goes to a pdf

        if 'Content-Type' in response.headers.keys():
            links_to_creeper = 'application/pdf' in str(response.headers['Content-Type'])
        else:
            return None

        ## Now find out how to search "MineCraft Creeper" under ebay


        # If it does, scrape it

        # If not, ignore it and move on to the next link

        # Write that data to the csv

        return