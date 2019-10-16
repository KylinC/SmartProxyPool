# -*- coding: utf-8 -*-
import requests
import json
from requests import Request,Session
from urllib import request, parse

from .baidu_sn import sn_calculator

class SendUrl(object):
    def send_url(self, url, headers, data=None):
        data= bytes(parse.urlencode(data), encoding='utf8')
        req = request.Request(url=url, data=data, headers=headers, method='POST')
        response = request.urlopen(req)
        return response.read().decode('utf-8')


class SendUrl2(object):
    def send_url(self, url, headers, data=None):
        s = Session()
        req = Request('post', url, data=data, headers=headers)
        prepped = s.prepare_request(req)
        r = s.send(prepped)
        return r.text

class SendUrl3(object):
    def send_url(self, url, headers, data=None):
        r = requests.post(url, data=data)
        return r.text

def get_baidu_response(ak, ip):
    sx = SendUrl3()
    sn = sn_calculator(ak)
    url = "https://api.map.baidu.com/location/ip"
    data = {"ip": ip, "ak": ak, "sn": sn, "coor": "bd09ll"}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    return sx.send_url(url, headers, data=data)

def get_ip_location(ak, ip):
    json_data = get_baidu_response(ak, ip)
    dict_data = json.loads(json_data)
    if 'content' in dict_data:
        return dict_data['content']['point'], dict_data['content']['address']
    else:
        return ({'x': '177.114129', 'y': '37.550339'}, '匿名')

if __name__ == '__main__':
    ak = "YcWN18KNNobNMU9NPt7NIGUF3eMdR1NS"
    ip = "114.239.110.85"
    print(get_ip_location(ak, ip))