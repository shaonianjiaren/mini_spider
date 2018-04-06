#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: jtf

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: jtfverygood@gmail.com

@software: garner

@file: url_table.py

@time: 18/4/5 下午5:56

@desc:url管理器，保存已处理url和未抓取url，并进行url去重
"""

class UrlTable(object):
    """
    url管理器，保存已处理url和未抓取url，并进行url去重
    """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        """
        判断是事有未爬取的url
        :return: true or false
        """
        return self.new_url_size() != 0

    def get_new_url(self):
        """
        获取一个未爬取的url
        :return: new url
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        将新的url添加到未爬取的url集合中
        :param url: string，新的url
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        return

    def add_new_urls(self, urls):
        """
        将一列新的url添加到未爬取的url集合中
        :param urls:
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
        return

    def new_url_size(self):
        """
        获取未爬取的url集合大小
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取已爬取的url集合大小
        :return:
        """
        return len(self.old_urls)