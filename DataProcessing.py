import hashlib
import json
import time
import random
import sqlite3
# 데이터 암호화
def sha512_hash(data):
    sha512_hash = hashlib.sha512(str(data).encode()).hexdigest()
    return sha512_hash
# 데이터 형변환
def listTostr(data):
    str_data = json.dumps(data)
    return str_data
# 데이터 형변환
def strTolist(data):
    list_data = json.loads(data)
    return list_data
# 현재 시간 반환
def now_time():
    return time.strftime("%Y-%m-%d", time.localtime(time.time()))
# 테스트용 랜덤한 숫자 생성
def generate_random_number(Number_):
    min_value = 10 ** (Number_ - 1)
    max_value = (10 ** Number_) - 1
    random_number = random.randint(min_value, max_value)
    return int(random_number)
def delete():
    conn = sqlite3.connect("database/bookmate.db")
    cur = conn.cursor()
    conn.execute("DELETE FROM StudentsData").rowcount
    conn.execute("DELETE FROM Book").rowcount
    conn.commit()
    cur.close()
    conn.close()