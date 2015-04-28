__author__ = 'Jason'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from chow_sort.items import ChowSortItem


class ChowSpider(CrawlSpider):
    name = "chow"
    start_urls = [
        'http://www.chow.com/recipes'
    ]

    rules = (
        Rule(LinkExtractor(allow=('.*',),
                           restrict_xpaths='//div[@class="chow_pagination"]/div[@class="pagination"]/a[@rel="next"]'),
             follow=True,
             callback='parse_recipes'),
    )

    def parse_recipes(self, response):
        for sel in response.xpath('//ul[@id="main_recipes"]/li/div'):
            item = ChowSortItem()
            item['name'] = sel.xpath('a/div[@class="image_link_overlay"]/div[@class="image_link_title"]/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['votes'] = sel.xpath('a/div[@class="image_link_overlay"]/div[@class="image_link_metric"]/text()').extract()

            yield item

    def parse_start_url(self, response):
        return self.parse_recipes(response)