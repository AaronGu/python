#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import webbrowser
import time
url1 = 'http://www.youku.com'
url2 = 'http://actives.youku.com/task/signv2/index'
#webbrowser.open(url1,new = 0,autoraise = True)
webbrowser.open(url2,new = 0,autoraise = True)
webbrowser.get()
print "Successed"
time.sleep(5)
webbrowser.close(webbrowser.get())

