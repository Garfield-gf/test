
import scrapy

class HuangSpider(scrapy.Spider):
    name = 'images'
    start_urls = ['http://w1.97xzjpzz.top/pw/thread.php?fid=15']

    def parse(self, response):
        print(response)
        title_list = response.xpath('//*[starts-with(@id,"a_ajax_")]/text()').extract()
        for i in title_list:
            print(i)