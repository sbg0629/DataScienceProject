import hashlib
import json
import time
import random
def sha512_hash(data):
    sha512_hash = hashlib.sha512(str(data).encode()).hexdigest()
    return sha512_hash

def listTostr(data):
    str_data = json.dumps(data)
    return str_data

def strTolist(data):
    list_data = json.loads(data)
    return list_data

def now_time():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))

def generate_random_number(Number_):
    min_value = 10 ** (Number_ - 1)
    max_value = (10 ** Number_) - 1
    random_number = random.randint(min_value, max_value)
    return int(random_number)