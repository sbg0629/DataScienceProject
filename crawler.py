# 크롤링을 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 경로 설정을 위한 모듈
import os

# 딜레이를 위한 모듈
import time

# 함수 작동 중 오류가 발생하면 0을 반환하고, 오류가 없으면 리스트를 반환
def book_list(id, pw, ReturnData=1):
    # 전체 작동 시간 측정 시작부분
    start = time.time()

    # try, except가 하나의 묶음
    # try 문에서 오류가 발생하면 크롬 드라이버가 없다는 오류 메시지를 출력하고 0을 반환
    try:
        # 크롬 드라이버 경로 설정 및 크롬 드라이버 실행
        driver_path = os.getcwd() + "\chromedriver.exe"
        driver = webdriver.Chrome(driver_path)
    except:
        print("크롬 드라이버가 없거나 버전이 다릅니다. chromedriver.exe를 다운받아 현재 디렉토리에 넣어주세요.")
        return 0
    driver.maximize_window()

    # 도서관 홈페이지 접속
    try:
        driver.get("https://lib.deu.ac.kr/")
    except:
        print("페이지가 응답이 없습니다.")
        return 0
    
    # XPATH를 이용해 로그인 버튼 클릭
    driver.find_element(By.XPATH, "/html/body/form[1]/header/div/div[1]/ul/li[4]/a").click()

    # 페이지 로딩을 위해 60초 대기 로딩이 끝나면 60초가 다 안 지나도 다음 코드로 넘어감
    driver.implicitly_wait(60)

    # 로그인 창에서 아이디와 비밀번호를 입력하고 엔터를 누름
    inputs = driver.find_elements(By.CLASS_NAME, "form-control")
    inputs[0].send_keys(id)
    inputs[1].send_keys(pw, Keys.ENTER)
    
    # 1초 대기
    time.sleep(1)

    # 아이디와 비밀번호가 틀렸을 경우 오류 메시지가 뜨고 오류 메시지를 확인하는 코드
    try:
        # 오류 메시지가 뜨면 오류 메시지를 확인하고 확인 버튼을 누름
        driver.switch_to.alert.accept()
        print("로그인 실패")
        driver.close()
        return 0
    
    # 오류 메시지가 뜨지 않으면 오류가 발생하지 않았다는 뜻이므로 pass
    except:
        print("로그인 성공")
        pass

    # 대출 기록 페이지로 이동
    driver.get("https://lib.deu.ac.kr/lend_lend.mir")
    # driver.implicitly_wait(60)

    bookdatalist = []
    # 1 도서 등록번호 저장, 기본 값
    if ReturnData == 1:
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-center")
        for datalist in SeleniumBookList[2::2]:
            bookdatalist.append(datalist.text)
    # 2 도서 이름, 저자 저장
    elif ReturnData == 2:
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-left")
        for bookdata in SeleniumBookList[1:]:
            bookdata = bookdata.text.split('/')
            bookdatalist.append(bookdata)
    # 3 도서 등록 번호, 도서 이름, 저자 저장
    elif ReturnData == 3:
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-center")
        for datalist in SeleniumBookList[2::2]:
            bookdatalist.append([datalist.text])
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-left")
        count = 0
        for bookdata in SeleniumBookList[1:]:
            bookdata = bookdata.text.split('/')
            for BookNameOrWriter in bookdata:
                bookdatalist[count].append(BookNameOrWriter)
            count += 1
    # 4 도서 등록 번호, 도서 이름
    elif ReturnData == 4:
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-center")
        for datalist in SeleniumBookList[2::2]:
            bookdatalist.append([datalist.text])
        SeleniumBookList = driver.find_elements(By.CLASS_NAME, "text-left")
        count = 0
        for bookdata in SeleniumBookList[1:]:
            bookdatalist[count].append(bookdata.text.split('/')[0])
            count += 1
    # 크롬 드라이버 종료
    driver.close()
    
    # 전체 작동 시간 측정 종료 및 출력
    print("크롤링 시간 {:.2f}초\n".format(time.time() - start))

    # bookcodelist가 비어있으면 대출 기록이 없다는 메시지를 출력하고 1을 반환
    if len(bookdatalist) == 0:
        print("대출 기록이 없습니다.")
        return 1
    
    # bookcodelist가 비어있지 않으면 bookcodelist를 반환
    return bookdatalist

def ListToTextFile(x):
    f = open("BookList.txt", "w")
    for i in x:
        print(i)
        f.write(f"{str(i)}\n")
    f.close()