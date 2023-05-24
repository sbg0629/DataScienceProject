# 크롤링을 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 딜레이를 위한 모듈
import time
# 정규식을 위한 모듈
import re

def recomand(code, test=False):
    list = []
    for i in code:
        driver = webdriver.Chrome()
        # 도서관 홈페이지 접속
        try:
            driver.get("https://lib.deu.ac.kr/")
        except:
            print("페이지가 응답이 없습니다.")
            return 0
        # 페이지 최대화
        driver.maximize_window()

        # 페이지 로딩을 위해 3초 대기 로딩이 끝나면 3초가 다 안 지나도 다음 코드로 넘어감
        driver.implicitly_wait(3)

        driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys(i, Keys.ENTER)
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "book_title").click()

        for j in range(1, 4): # 사이트 분야 Best 도서 3개를 돌리는 for 문
            xpath = '//*[@id="data_data_lend_best_scope"]/div/div[2]/ul/li[{}]/a/dl/dt'.format(j)
            bestlist = driver.find_element(By.XPATH, xpath).text
            bestlistname = re.sub(r'\s*/.*$', '', bestlist)
            list.append(bestlistname)
        driver.quit()
    print(list)
    return list

recomand(["E000994079", "E000593984"])