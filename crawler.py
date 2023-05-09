from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

def book_list(id, pw, test=False):
    start = time.time()
    try:
        driver_path = os.getcwd() + "\chromedriver.exe"
        driver = webdriver.Chrome(driver_path)
    except:
        print("크롬 드라이버가 없습니다. chromedriver.exe를 다운받아 현재 디렉토리에 넣어주세요.")
        return
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

    print("\n\n대출 목록 불러오는 중...\n")
    try:
        # driver.implicitly_wait(3)
        research = driver.find_element(By.CLASS_NAME, "btn btn_mir_view btn-sm")
        research.click()
    except:
        print("대출 기록을 조회에 실패했습니다.")
    if test:
        for i in range(30):
            print(i + 1)
            time.sleep(1)
    print("대출 목록 불어오기 완료")
    driver.close()
    
    if test == False:
        print("크롤링 시간 {:.2f}초".format(time.time() - start))
    else:
        print("크롤링 시간 {:.2f}초".format(time.time() - start - 30))