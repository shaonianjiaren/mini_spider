#!/usr/bin/env python
#-*-coding:utf-8 -*-

"""

@author: caopeng

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: deamoncao100@gmail.com

@software: garner

@file: task_manager.py

@time: 18/4/8 下午5:19

@desc:
"""

import random
import time
import Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    """
    将创建的两个队列注册在网络上，利用register方法
    """
    pass

#将queue对象暴露在网络上,可以通过方法获取
QueueManager.register("get_task_queue", callable=lambda:task_queue)
QueueManager.register("get_result_queue", callable=lambda:result_queue)

#绑定端口，设置口令
manager = QueueManager(address=("127.0.0.1", 8001), authkey="root")

#启动管理，监听信息通道
manager.start()

#通过管理实例的方法获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#添加任务
for url in ["ImageUrl_" + str(i) for i in range(10)]:
    print "put task %s ...." % url
    task.put(url)

#获取返回结果
print "try get result ..."
for i in range(10):
    print "result is %s" % result.get(timeout=10)

manager.shutdown()

