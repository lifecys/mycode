# -*- coding: utf-8 -*-
import scrapy

from tencenthr.items import TencenthrItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        item = TencenthrItem()
        trs = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in trs:
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[4]/text()").extract_first()
            item["count"] = tr.xpath("./td[3]/text()").extract_first()
            item["cls"] = tr.xpath("./td[2]/text()").extract_first()
            item["publish_data"] = tr.xpath("./td[5]/text()").extract_first()
            yield item

            next_url = response.xpath("//a[@id='next']/@href").extract_first()

            if next_url != "javascript:;":
                next_url = "https://hr.tencent.com/" + next_url
                yield scrapy.Request(
                    next_url,
                    callback=self.parse
                )
