__author__ = 'admin'
# -*- coding: utf-8 -*-
import urllib
import time

def getStockDealData(stockCode):
    try:
       dataUrl = "http://stockpage.10jqka.com.cn/spService/"+stockCode+"/Funds/realFunds"
       stdout = urllib.urlopen(dataUrl)
       print stdout
       stdoutInfo = stdout.read().decode('gb2312')
       stdoutInfo=eval(stdoutInfo)
       realDeal=[]
       for i in stdoutInfo['flash']:
           realDeal.append(i["sr"])
    except Exception as e:
        print(">>>>>> Exception: " + str(e))
    finally:
        None
if __name__ == '__main__':
   start=time.clock()
   getStockDealData("600000")
   end=time.clock()
   print end-start

