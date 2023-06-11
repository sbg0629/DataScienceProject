from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.family'] = 'Malgun Gothic'

def category(name):
    driver = webdriver.Chrome()
    driver.get("https://www.kyobobook.co.kr/")
    driver.implicitly_wait(60)

    driver.find_elements(By.CLASS_NAME, "ip_gnb_search")[0].send_keys(name, Keys.ENTER)
    driver.implicitly_wait(60)

    driver.find_elements(By.CLASS_NAME, "prod_info")[0].click()
    driver.implicitly_wait(60)

    book_category = driver.find_elements(By.CLASS_NAME, "btn_sub_depth")[-1].text

    driver.quit()

    return book_category

list1 = ["비욘드 그래비티", "마이클센델 정의란 무엇인가", "오늘밤 세계에서 이 사랑이 사라진다 해도"] #test_list

p = []
for row in list1:
    category_name = category(row)
    category_name = category_name.replace("/", "")  # Remove special characters
    p.append(category_name)

# 그래프 생성 #손봉균의 마무으리~
plt.pie(np.ones(len(p)), labels=p, autopct='%.2f')

# 그래프를 이미지 파일로 저장
plt.savefig("pie_data.png")

# 이미지 파일 삭제
if os.path.exists("pie_data.png"):
    os.remove("pie_data.png")
    print("이미지 파일이 삭제되었습니다.")

plt.show()