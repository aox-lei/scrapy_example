# -*- coding: utf-8 -*-
import scrapy
from ccidcom.items import DocumentItem


# 自动创建完以后, scrapy会自动加一个spider
# 变成CcidcomspiderSpider, 不太好看, 所以自己改一下类名, CcidcomSpider
class CcidcomSpider(scrapy.Spider):
    # 爬虫的名称, 启动就靠这个了
    name = 'ccidcomSpider'
    # 允许请求的地址, 如果请求的域名不是这个, scrapy会自动过滤掉
    allowed_domains = ['www.ccidcom.com']
    # 开始的url, 可以有多个
    # 不过咱们需要改成http://www.ccidcom.com/yaowen/index.html
    start_urls = ['http://www.ccidcom.com/yaowen/index.html']

    def parse(self, response):
        # item = DocumentItem()
        # 从html代码中解析获取到所有的文章列表的标签
        document_list = response.css('div.artlisting div.article-item')
        for document in document_list:
            # 解释一下getall和get的区别
            # getall, 会获取到所有匹配的选择器, 返回的是个可循环的list,
            # get只返回匹配的第一个
            # 里面是css选择器, 稍后会具体讲解, ::attr是获取到指定标签的属性的值
            # 从a标签中拿到文章页的url
            url = document.css('div.title a::attr("href")').get()
            # 因为获取的url没有域名, 所以补充一下
            url = 'http://www.ccidcom.com{}'.format(url)
            # yield可以当成返回一个请求, scrapy.Request会构造一个请求, 这个请求是get
            # callback, 会把下载器返回的Response(资源对象)传给咱们指定的方法parse_document

            yield scrapy.Request(url, callback=self.parse_document)

    def parse_document(self, response):
        # 实例化一个item对象, 用来存放数据
        item = DocumentItem()
        item['url'] = response.url  # 请求的url
        # 从response使用css选择器读取到数据然后赋值给item
        item['title'] = response.css('div.heading::text').get()
        item['writer'] = response.css('div.author::text').get()
        item['publish_time'] = response.css('div.pub-time::text').get()
        item['source'] = response.css('div.source::text').get()
        item['content'] = response.css('div.content').get()

        yield item
