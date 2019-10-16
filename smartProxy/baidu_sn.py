# -*- coding: utf-8 -*- 
import urllib
import urllib.parse
import hashlib

def sn_calculator(yourak):
    # 以get请求为例http://api.map.baidu.com/location/ip
    queryStr = '/location/ip'
    encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    rawStr = encodedStr + yourak
    return hashlib.md5((urllib.parse.quote_plus(rawStr)).encode("utf-8")).hexdigest()

if __name__ == '__main__':
    print(sn_calculator("YcWN18KNNobNMU9NPt7NIGUF3eMdR1NS"))