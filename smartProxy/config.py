# Scheduler 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 目标网站
TEST_URL = 'http://www.baidu.com'

# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，default = None
REDIS_PASSWORD = "passpass"
REDIS_KEY = 'proxies'

# selection initial ruler
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# selection parameter
RANDOM_INTERVAL = [90, 100]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 响应码
VALID_STATUS_CODES = [200, 302]

# 最大批测试量
BATCH_TEST_SIZE = 10