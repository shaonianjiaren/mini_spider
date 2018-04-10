#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: jtf

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: jtfverygood@gmail.com

@software: garner

@file: webpage_save.py

@time: 18/4/6 下午2:42

@desc:保存网页
"""

import codecs
import time

class WebPageSave(object):
    """
    保存网页
    """

    def __init__(self):
        self.filepath = "news_%s.html" % (time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def save_data(self, data):
        """
        存储数据
        :param data:
        :return:
        """
        if data is None:
            return
        self.datas.append(data)
        return

    def output_head(self, path):
        """
        将html头写进去
        :param path:
        :return:
        """
        fout = codecs.open(path, "w", encoding="gb2312")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self):
        """
        输出html
        :return:
        """
        fout = codecs.open('/usr/local/nginx/html/baike.html', 'w', encoding='gb2312')
        for data in self.datas:
            try:
                fout.write("<tr>")
                fout.write("<td><a href='%s'>%s</a></td>" % (data["url"], data['title']))
                #fout.write("<td>%s</td>" % data["title"])
                #fout.write("<td>%s</td>" % data["summary"])
                fout.write("</tr>")
            except Exception as e:
                continue
        fout.close()

    def output_end(self, path):
        """
        输出html结束
        :param path: 文件存储路径
        :return:
        """
        fout = codecs.open(path, "w", encoding="gb2312")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

