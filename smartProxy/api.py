from flask import Flask, g, render_template, request, url_for, Response
import flask
import json
from .database import RedisClient
from .test_get_ip import *
from .baidu_sn import *
from .config import AK

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/data', methods=['POST','GET'])
def data():
    callback = flask.request.args.get('callback')
    conn = get_conn()
    ip_test = conn.random()
    ip_test_split = ip_test.split(":")
    ak_test = get_ip_location(AK, ip_test_split[0])
    location = [float(ak_test[0]['x']), float(ak_test[0]['y'])]
    data = {"value": 95, "ip": ip_test, "lg":location}
    json_data = json.dumps(data)
    return Response('{}({})'.format(callback, json_data))

@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run(debug=True)