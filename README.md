# SmartProxyPool

>  A complete-auto IP pool, provider IP location visualization. 
>
>  网络爬虫IP池自动筛选系统

<img src='https://img.shields.io/badge/python-3.5.7-blue.svg'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/Redis-3.0.6-red'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/flask-1.1.1-brightgreen'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/jquery-1.11.2-yellowgreen'  align='left' style=' width:100px'/></br>

This project provide a web API for auto Proxy Pool, automatically crawl IP proxy from xici.com, 66ip.cn, kuaidaili.com and some GitHub opensource ip proxy project. Once you install this project on your Linux server, you can get a dynamic proxy from your server port 5555.

## View

![](https://tva1.sinaimg.cn/large/006y8mN6gy1g7zvm610i3j31qb0u0tbk.jpg)

> Random select a Available IP from database. 



![](https://tva1.sinaimg.cn/large/006y8mN6gy1g7zvm59zlsj31qu0u0mzt.jpg)

> Find Accurate IP location



## Launch 

- Clone this project

```
git clone https://github.com/KylinC/SmartProxyPool.git
```

- install redis and other dependent packages (sever)

```
// install redis
sudo apt-get install redis-server

//install packages
cd SmartProxy
pip install -r requirements.txt
```

- Change the redis' password to yours (SmartProxy/SmartProxy/config.py)

```python
# Scheduler Switch
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# Check Loop
TESTER_CYCLE = 20
# CRAWLER Loop
GETTER_CYCLE = 300

# API Configuration
API_HOST = '127.0.0.1'
API_PORT = 5000                 ##### Flask Configuration

# Aim Website
TEST_URL = 'http://www.baidu.com'     ##### Aim Website you want to crawler

# Redis Database locstion
REDIS_HOST = '127.0.0.1'         ###### Support Your Remote Redis Database

# Redis port
REDIS_PORT = 6379

# Redis password，default = None
REDIS_PASSWORD = "YourPassword"         ##### Change to Your Redis Password
REDIS_KEY = 'proxies'

# selection initial ruler
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# selection parameter
RANDOM_INTERVAL = [90, 100]

# redis mox data number
POOL_UPPER_THRESHOLD = 50000

# accept response code
VALID_STATUS_CODES = [200, 302]

# ip test batch
BATCH_TEST_SIZE = 10

# baiduMap AK
AK = "YourAK"  #### Change to your Baidu Map API AK
```

- turn on your redis server(refers to SmartProxy/instructions)
- Run it on your server

```
python run.py
```

## Port

### - Visualization

View in Browser(recommend: Google Chrome) at **http://YourServerIP:YourPort/**

### - Get IP

Access in WebSpider Programm at **http://YourServerIP:YourPort/random**



According to **Python3WebSpider** written by Qingcai Cui.