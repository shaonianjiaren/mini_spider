#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: jtf

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: jtfverygood@gmail.com

@software: garner

@file: mini_spider.py

@time: 18/4/6 下午2:55

@desc:主程序入口
"""

import url_table
import crawl
import webpage_parse
import webpage_save

class MiniSpider(object):
    """
    小蜘蛛
    """

    def __init__(self):
        self.url_table = url_table.UrlTable()
        self.crawl = crawl.Crawl()
        self.webpage_parse = webpage_parse.WebPageParse()
        self.webpage_save = webpage_save.WebPageSave()

    def crawler(self, root_url):
        """
        添加入口url
        :param root_url: 入口url
        :return:
        """
        self.url_table.add_new_url(root_url)
        while(self.url_table.has_new_url() and self.url_table.old_url_size() < 100):
            try:
                #从url管理器获取新的url
                new_url = self.url_table.get_new_url()
                #网页下载器下载网页
                html = self.crawl.download(new_url)
                #网页解析器解析网页数据
                new_urls, data = self.webpage_parse.parse(new_url, html)
                #将抽取的url添加到url管理器中
                self.url_table.add_new_urls(new_urls)
                #存储网页
                self.webpage_save.save_data(data)
                print "已经抓取%s个链接" % self.url_table.old_url_size()
            except Exception as e:
                print "crawl failed"
        self.webpage_save.output_html()


if __name__ == '__main__':
    mini_spider = MiniSpider()
    mini_spider.crawler("http://news.163.com/18/0406/12/DEN902I70001875O.html")

