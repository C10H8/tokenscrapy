import scrapy
import re
import logging
import json
from tokenscrapy.items import TokenscrapyItem



class QuotesSpider(scrapy.Spider):
    name = "tokens"
    urls = [
        'https://etherscan.io/tokens?sort=marketcap&order=desc',
    ]
    p = re.compile(r'[(](.*)[)]', re.S)

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for token in response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr'):
            item = TokenscrapyItem()
            id = token.xpath('./td/b/span[@style="position:relative; top:8px"]/text()').extract_first()[1:]
            item["id"] = int(id)
            item["image_url"] = response.urljoin(token.xpath('./td[@align="center"]/a/img/@src').extract_first())
            margin = token.xpath('./td/h5/a/text()').extract_first()
            find_res = re.findall(self.p, margin)
            item["name"] = find_res[0]
            item["example"] = margin.replace('('+find_res[0]+')', '')
            item["des"] = token.xpath('./td/small/font/text()').extract_first()
            item["price"] = token.xpath('./td/span/text()').extract_first()
            item["change"] = token.xpath('./td/font[@class="text-nowrap"]/text()').extract_first()
            item["volume"] = token.xpath('./td/text()').extract()[-2]
            item["market_cap"] = token.xpath('./td/text()').extract()[-1][:-3]
            yield item

        next_page_url = response.xpath('//a[@class="btn btn-default btn-xs logout"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

