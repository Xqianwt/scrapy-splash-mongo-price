# -*- coding: utf-8 -*-
import scrapy
from price.items import PriceItem
from scrapy_splash import SplashRequest

script = """
function main(splash, args)
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(args.wait))
    return {
        html = splash:html(),
    }
end
"""

class MofcomSpider(scrapy.Spider):
    name = 'mofcom'
    allowed_domains = ['nc.mofcom.gov.cn']
    start_urls = ['http://nc.mofcom.gov.cn/']

    def start_requests(self):
        # http://nc.mofcom.gov.cn/channel/jghq2017/market_list.shtml?province=340000
        provinces = self.settings.get('PROVINCES')
        base_url = 'http://nc.mofcom.gov.cn/channel/jghq2017/market_list.shtml?province='
        for province in provinces:
            url = base_url + province
            yield SplashRequest(url, callback=self.Market_parse, endpoint='execute',args={'lua_source': script, 'wait': 5})


    def Market_parse(self, response):
        markets = response.xpath('//ul[@class="marketList"]/li')

        for market in markets:
            #item = MarketItem()
            href = market.xpath('./h1/a/@href').extract()[0]  
            url = self.start_urls[0] + href         
            yield SplashRequest(url, callback=self.parse, endpoint='execute',args={'lua_source': script, 'wait': 5})

##\Users\14307\tutorial\price>
    def parse(self, response):
        products = response.xpath('//table/tbody/tr')

        for product in products[1:]:
            item = PriceItem()

            item['date'] = product.xpath('./td[1]/text()').extract()[0]  
            item['product'] = product.xpath('./td[2]/span/text()').extract()[0]  
            item['price'] = product.xpath('./td[3]/span/text()').extract()[0]  
            item['market'] = product.xpath('./td[4]/a/text()').extract()[0]  
            yield item


        
  
        
