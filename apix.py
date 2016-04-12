import time
import json
import datetime
__author__ = 'admin'
import requests

def stock():
    start=time.clock()
    url = "http://a.apix.cn/apixmoney/stockdata/stock"
    global relprice
    querystring = {"stockid":"sz000670"}

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'apix-key': "2583488c206b4d2e654d9db7add7fdab"
        }
    relprice=0
    response = requests.request("GET", url, headers=headers, params=querystring)
    print datetime.datetime.now()
    price=json.loads(response.text)['data']['stockinfo']['auctionPrice']

    if relprice!=price:
        print price
        relprice=price

    end=time.clock()
    print end-start
if __name__=="__main__":
    for i in range(10000):
        stock()