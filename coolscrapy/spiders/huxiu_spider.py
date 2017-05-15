# -*- coding: utf-8 -*-
from coolscrapy.items import HuxiuItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import chardet
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class HuxiuSpider(CrawlSpider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/index.php"
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'/article/\d+.html',)), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        detail = response.xpath('//div[@class="article-wrap"]')
        item = HuxiuItem()
        item['image_url'] = detail.xpath('div[@class="article-img-box"]/img/@src').extract_first()
        item['title'] = detail.xpath('h1/text()').extract_first()
        item['link'] = response.url
        item['posttime'] = detail.xpath('div[@class="article-author"]/div[@class="column-link-box"]/span[@class="article-time pull-left"]/text()').extract_first()
        yield item
