import time

__author__ = 'admin'
import requests
start=time.clock()
url = "http://a.apix.cn/apixmoney/stockdata/stock"

querystring = {"stockid":"sz000670"}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'apix-key': "2583488c206b4d2e654d9db7add7fdab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


end=time.clock()
print end-start