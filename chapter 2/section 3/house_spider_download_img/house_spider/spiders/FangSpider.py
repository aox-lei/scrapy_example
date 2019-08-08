# -*- coding: utf-8 -*-
import scrapy
from house_spider.items import HouseItem, HouseItemLoader, CommunityItem, CommunityItemLoader


class FangSpider(scrapy.Spider):
    '''
    下载项目图片
    '''
    name = 'FangSpider'
    allowed_domains = ['fang.com']

    def start_requests(self):
        yield scrapy.Request(url='https://esf.fang.com',
                             cookies={
                                 'city':
                                 'www',
                                 'global_cookie':
                                 'tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc',
                                 'unique_cookie':
                                 'U_tixt3tpiedn0brb7m4t9pl9fd2zjyb8wtwc'
                             },
                             dont_filter=True,
                             callback=self._start_request,
                             meta={'cookiejar': 1})

    def _start_request(self):
        yield self.request_list()

    def request_list(self, page=1):
        if page > 1:
            url = 'https://esf.fang.com/house/i3{page}/'.format(page=page)
        else:
            url = 'https://esf.fang.com/'

        return scrapy.Request(url,
                              callback=self.parse,
                              dont_filter=True,
                              meta={
                                  'page': page,
                                  'cookiejar': 1
                              })

    def parse(self, response):
        tr_list = response.css('div.shop_list dl')
        # 有时候房天下会301跳转一次才过来, 而301跳转后, 元素就变成了shop_list, 直接访问就是houseList
        info_css_rule = 'dd > h4 > a::attr("href")'
        if not tr_list:
            tr_list = response.css('div.houseList dl')
            info_css_rule = 'dd > p.title > a::attr("href")'

        if tr_list:
            for info in tr_list:
                info_url_css = info.css(info_css_rule)
                if info_url_css:
                    yield response.follow(info_url_css[0],
                                          callback=self.parse_house_info,
                                          dont_filter=True)

    def parse_house_info(self, response):
        item = HouseItemLoader(HouseItem(), response)
        item.add_css('title', '#lpname > h1::text')
        item.add_css(
            'total_price',
            'div.tab-cont-right > div.tr-line.clearfix.zf_new_title > div.trl-item_top > div.trl-item.price_esf.sty1 > i::text'
        )
        item.add_css(
            'area',
            'div.tab-cont-right > div:nth-child(3) > div.trl-item1.w182 > div.tt::text'
        )
        item.add_css(
            'direction',
            'div.tab-cont-right > div:nth-child(4) > div.trl-item1.w146 > div.tt::text'
        )
        item.add_css('community', 'div.rcont > a::text')
        item.add_value('url', response.url)

        # 处理图片
        images_list = response.css('ul.litImg li')
        if images_list:
            for image in images_list:
                item.add_css('image_urls', 'img::attr("data-src2")')

        yield item.load_item()

    def parse_community(self, response):
        item = CommunityItemLoader(CommunityItem(), response)
        item.add_css('name', 'div.ceninfo_sq > h1 > a::text')
        item.add_css(
            'address',
            'div.con_left > div:nth-child(1) > div.inforwrap.clearfix > dl > dd:nth-child(1)::attr("title")'
        )
        item.add_css(
            'area',
            'div.con_left > div:nth-child(1) > div.inforwrap.clearfix > dl > dd:nth-child(2)::text'
        )
        yield item.load_item()
