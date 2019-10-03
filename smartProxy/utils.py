import requests
import random
from requests.exceptions import ConnectionError
from .baseData import user_agents

def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    user_agent = random.choice(user_agents)
    base_headers = {
        'User-Agent': user_agent,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
    }

    headers = dict(base_headers, **options)
    print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None


if __name__ == '__main__':
    print(get_page('http://www.baidu.com'))