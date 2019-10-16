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