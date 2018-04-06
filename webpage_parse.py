#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: jtf

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: jtfverygood@gmail.com

@software: garner

@file: webpage_parse.py

@time: 18/4/6 下午2:08

@desc:网页解析器
"""

import re
import urlparse
from bs4 import BeautifulSoup as bs

class WebPageParse(object):
    """
    网页解析器
    """

    def parse(self, page_url, html_cont):
        """
        用于解析网页内容，抽取url和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载的网页内容
        :return: 返回url和数据
        """
        if page_url is None or html_cont is None:
            return
        soup = bs(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        抽取有效url
        :param page_url: 下载页面的url
        :param soup:
        :return: 返回新的url集合
        """
        new_urls = set()
        # 抽取符合要求的a标记，a标签，且href能匹配到正则,links为一系列tag集合
        links = soup.find_all('a', href=re.compile(r'http://news|home|ent.163.com/.*.html#.*'))
        for line in links:
            #提取href属性
            new_url = line['href']
            # 拼接完整网址
            #new_full_url = urlparse.urljoin(page_url, new_url)
            #new_urls.add(new_full_url)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        抽取有效数据
        :param page_url: 下载页面的url
        :param soup:
        :return: 返回有效数据
        """
        data = {}
        data['url'] = page_url
        title = soup.find('div', class_='post_content_main').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='post_text')
        data['summary'] = summary.get_text()
        return data
