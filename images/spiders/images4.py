# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagesItem


class Images4Spider(CrawlSpider):
    name = 'images4'
    allowed_domains = ['w1.97xzjpzz.top']
    start_urls = ['http://w1.97xzjpzz.top/pw/thread.php?fid=15']
    get_links = []

    rules = (

        Rule(LinkExtractor(allow=r'http://w1.97xzjpzz.top/pw/html_data/15/1910/\d+.html'), callback='parse_item',
             follow=False),
        Rule(LinkExtractor(allow=r'http://w1.97xzjpzz.top/pw/thread.php\?fid=15&page=\d+')),
    )

    def parse_item(self, response):
        item = ImagesItem()

        print(response.url)

        # list1=[]
        ref = response.xpath('//*[@id="read_tpc"]/img/@src').extract()
        print(ref)
        # list1.append(ref)
        # item['image_urls'] = list1
        item['image_urls'] = ref


        return item
