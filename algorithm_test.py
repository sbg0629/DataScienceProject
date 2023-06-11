# 크롤링을 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 딜레이를 위한 모듈
import time
# 정규식을 위한 모듈
import re

def recommand(code):
    list = {}
    driver = webdriver.Chrome()
    try:
        driver.get("https://lib.deu.ac.kr/")
    except:
        print("페이지가 응답이 없습니다.")
        return 0
    # 도서관 홈페이지 접속

    # 페이지 최대화
    driver.maximize_window()

    # 페이지 로딩을 위해 3초 대기 로딩이 끝나면 3초가 다 안 지나도 다음 코드로 넘어감
    driver.implicitly_wait(3)
    if type(code) is str:
        print(f"code: {code}\n단일 검색")
        driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys(code, Keys.ENTER)
        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "book_title").click() # 검색하면 나오는 책 클릭

        bookinfo = driver.find_element(By.XPATH, '//*[@id="panel"]/div[2]/div/div[1]/div/h4')
        bookname = bookinfo.text.split('/')[0]

        bestlistname = []

        elements = driver.find_elements(By.XPATH, '//*[@id="data_data_lend_best_scope"]/div/div[2]/ul/li/a/dl/dt')

        for element in elements:
            bestlistname.append(re.sub(r'\s*/.*$', '', element.text))

        if bestlistname:
            list[bookname] = bestlistname
        else:
            list[bookname] = "해당되는 책의 추천책이 없습니다."
    else:
        print(f"code: {code}\n리스트 검색")
        for i in code:
            driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys(i, Keys.ENTER) # 검색창에 책 코드 입력
            time.sleep(3)

            driver.find_element(By.CLASS_NAME, "book_title").click() # 검색하면 나오는 책 클릭

            bookinfo = driver.find_elements(By.XPATH, '//*[@id="panel"]/div[2]/div/div[1]/div/h4') # 책의 이름과 저자가 /로 구분되어있는 문자열을 저장
            bookname = bookinfo.text.split('/')[0]

            bestlistname = [] # 추천 책이 담길 리스트

            elements = driver.find_elements(By.XPATH, '//*[@id="data_data_lend_best_scope"]/div/div[2]/ul/li/a/dl/dt') # 추천 책을 elements에 저장

            for element in elements:
                bestlistname.append(re.sub(r'\s*/.*$', '', element.text)) # 추천되는 책의 제목만 사용

            if bestlistname:
                list[bookname] = bestlistname # 추천되는 책들을 딕셔너리 value에 리스트로 저장
            else:
                list[bookname] = "해당되는 책의 추천책이 없습니다." # 그 책의 분야의 추천 책이 없을 경우 출력

            driver.find_element(By.XPATH, "/html/body/form/header/div/div/h1/a/img").click() # 다시 검색창으로 이동
    

    driver.quit()
    return list # 리스트 리턴

# 책 카테고리를 알려주는 함수
def category(names):
    book_categorys = []
    driver = webdriver.Chrome()
    if type(names) is str:
        names = [names]
    for name in names:
        driver.get("https://www.kyobobook.co.kr/")
        driver.implicitly_wait(60)

        # 책 이름 검색
        driver.find_elements(By.CLASS_NAME, "ip_gnb_search")[0].send_keys(name, Keys.ENTER)
        driver.implicitly_wait(60)
        
        # 검색 목록에서 첫번째 책 클릭
        driver.find_elements(By.CLASS_NAME, "prod_info")[0].click()
        driver.implicitly_wait(60)

        # 책 분야 확인
        book_category = driver.find_elements(By.CLASS_NAME, "btn_sub_depth")[2].text
        book_categorys.append(book_category)
        print(f"{name}의 분야: {book_category}")
    driver.close()

    return book_categorys