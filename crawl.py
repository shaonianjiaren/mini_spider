#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: jtf

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: jtfverygood@gmail.com

@software: garner

@file: crawl.py

@time: 18/4/6 下午2:04

@desc:网页抓取器
"""

import requests

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"


class Crawl(object):
    """
    下载器
    """

    def download(self, url):
        """
        下载网页
        :param self:
        :param url: string
        :return:
        """
        if url is None:
            return None
        headers = {"User-Agent": UA}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'gb2312'
            return r.text
        return None