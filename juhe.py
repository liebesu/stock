# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
import time

#----------------------------------
# 股票数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/21
#----------------------------------

def main():

    #配置您申请的APPKey
    appkey = "75f0d13db6ded8a7e8f29ed289088221"

    #1.沪深股市
    request1(appkey,"GET")

    #2.香港股市
    '''request2(appkey,"GET")

    #3.美国股市
    request3(appkey,"GET")

    #4.香港股市列表
    request4(appkey,"GET")

    #5.美国股市列表
    request5(appkey,"GET")'''

    #6.深圳股市列表
    request6(appkey,"GET")

    #7.沪股列表
    request7(appkey,"GET")



#沪深股市
def request1(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/hs"
    params = {
        "gid" : "sz000670", #股票编号，上海股市以sh开头，深圳股市以sz开头如：sh601009
        "key" : appkey, #APP Key

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    print content
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#香港股市
def request2(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/hk"
    params = {
        "num" : "", #股票代码，如：00001 为“长江实业”股票代码
        "key" : appkey, #APP Key

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#美国股市
def request3(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/usa"
    params = {
        "gid" : "", #股票代码，如：aapl 为“苹果公司”的股票代码
        "key" : appkey, #APP Key

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#香港股市列表
def request4(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/hkall"
    params = {
        "key" : appkey, #您申请的APPKEY
        "page" : "", #第几页,每页20条数据,默认第1页

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#美国股市列表
def request5(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/usaall"
    params = {
        "key" : appkey, #您申请的APPKEY
        "page" : "", #第几页,每页20条数据,默认第1页

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#深圳股市列表
def request6(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/szall"
    params = {
        "key" : appkey, #您申请的APPKEY
        "page" : "1", #第几页(每页20条数据),默认第1页

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"

#沪股列表
def request7(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/stock/shall"
    params = {
        "key" : appkey, #您申请的APPKEY
        "page" : "1", #第几页,每页20条数据,默认第1页

    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"



if __name__ == '__main__':
    starttime=time.clock()
    main()
    print time.clock()-starttime