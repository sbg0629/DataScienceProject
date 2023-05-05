from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

# 아이디, 비밀번호 가져오기
f = open('person_info.txt', 'r')
p_info = f.read().split('\n')
f.close()
test_id = p_info[0]
test_pw = p_info[1]

def book_list(test=False, id=test_id, pw=test_pw):
    driver_path = os.getcwd() + "\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    driver.get("https://lib.deu.ac.kr/")
    login_bnts = driver.find_element(By.XPATH, "/html/body/form[1]/header/div/div[1]/ul/li[4]/a")
    login_bnts.click()
    driver.implicitly_wait(3)
    inputs = driver.find_elements(By.CLASS_NAME, "form-control")
    inputs[0].send_keys(id)
    inputs[1].send_keys(pw, Keys.ENTER)
    driver.find_element(By.XPATH, "/html/body/form[1]/header/nav/div[1]/ul[2]/li[2]/a").click()
    time.sleep(3)
    driver.get("https://lib.deu.ac.kr/lend_lend.mir")
    if test:
        for i in range(30):
            print(i + 1)
            time.sleep(1)
    driver.close()