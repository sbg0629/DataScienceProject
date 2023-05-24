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
    # 페이지 최대화
    driver.maximize_window()
    
    # 페이지 로딩을 위해 3초 대기 로딩이 끝나면 3초가 다 안 지나도 다음 코드로 넘어감
    driver.implicitly_wait(3)

    driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys(code, Keys.ENTER)
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "book_title").click()

    driver.quit()