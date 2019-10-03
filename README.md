# SmartProxy

>  A complete-auto IP pool, provider IP location visualization. 

<img src='https://img.shields.io/badge/python-3.5.7-blue.svg'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/Redis-3.0.6-red'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/flask-1.1.1-brightgreen'  align='left' style=' width:100px'/></br>

<img src='https://img.shields.io/badge/jquery-1.11.2-yellowgreen'  align='left' style=' width:100px'/></br>

This project provide a web API for auto Proxy Pool, automatically crawl IP proxy from xici.com, 66ip.cn, kuaidaili.com and some GitHub opensource ip proxy project. Once you install this project on your Linux server, you can get a dynamic proxy from your server port 5555.

- Clone this project

```
git clone https://github.com/KylinC/SmartProxy.git
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
- turn on your redis server(refers to SmartProxy/instructions)
- Run it on your server

```
python run.py
```



According to **Python3WebSpider** written by Qingcai Cui.