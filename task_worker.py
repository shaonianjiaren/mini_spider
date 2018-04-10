#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: caopeng

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: deamoncao100@gmail.com

@software: garner

@file: task_worker.py

@time: 18/4/8 下午5:28

@desc:
"""

import time
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

#连接到服务器
server_addr = "127.0.0.1"
print "Connect to server %s ..." % server_addr

#端口与验证口令保持与服务进程一致
m = QueueManager(address=(server_addr, 8001), authkey="root")

#网络连接
m.connect()

#获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列获取任务，并将结果写入result队列
while not task.empty():
    image_url = task.get(True, timeout=5)
    print "run task download %s .." % image_url
    time.sleep(1)
    result.put("%s -------> success" % image_url)
print "worker exit"