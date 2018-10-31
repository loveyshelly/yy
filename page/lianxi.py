#coding=utf-8

import time
import datetime

t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(t)
t1=time.strftime('%Y-%m-%d %H:%M:%S')
print(t1)
day=(datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')
print(day)

