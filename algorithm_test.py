# 크롤링을 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 딜레이를 위한 모듈
import time

def recomand(code, test=False):

    driver = webdriver.Chrome()
    # 도서관 홈페이지 접속
    try:
        driver.get("https://lib.deu.ac.kr/")
    except:
        print("페이지가 응답이 없습니다.")
        return 0

    driver.find_element(By.XPATH, "/html/body/form[1]/header/div/div[2]/div/div/div/div/div/input").click()
    # 페이지 로딩을 위해 3초 대기 로딩이 끝나면 3초가 다 안 지나도 다음 코드로 넘어감
    driver.implicitly_wait(3)

    input_element = driver.find_element(By.CLASS_NAME, "form-control")
    input_element.send_keys(code, Keys.ENTER)

    driver.find_element(By.XPATH, "/html/body/form/section/section/section/div[2]/div[3]/form/div[1]/table/tbody/tr/td[2]/a").click()

    time.sleep(1)

    driver.quit()

recomand("E000906893")