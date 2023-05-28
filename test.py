from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키에 관련된 모듈 가져오기
import time
import sys #파일로 저장하기 위한 모듈
import os #폴더를 다루기 위한 모듈

import urllib.request
import urllib
import re #정규표현식 관련 '레귤러 익스프레션스'
import math #수학
import random #랜덤

#이미지를 저장할 폴더를 생성
f_dir = input('이미지를 저장할 폴더를 지정하세요.(예:c:\\test_img\\)>')

dir_name = '사진저장'

#저장될 파일 위치와 이름을 지정하기
now = time.localtime()

f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
#생성한 폴더로 이동
os.makedirs(f_dir+f_name+'-'+dir_name)#폴더생성
os.chdir(f_dir+f_name+'-'+dir_name)#폴더이동
f_result_dir= f_dir+f_name+'-'+dir_name #확인용 최종 폴더경로

print(f_result_dir)
#크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:\python_temp\chromedriver.exe"
driver = webdriver.Chrome(path)

#크롤링 시작 시간을 위한 타임스탬프를 찍습니다.
s_time = time.time()

#페이지 해당 경로로 열기
driver.get("https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid=be3db10c-b642-409c-81cc-c4cdecb5bd8b&temp=")
time.sleep(3)#로딩완료까지 3초 대기

#스크롤다운 함수를 생성한 후 실행합니다.
def scroll_down(driver):
    #scrollHeight = 창사이즈, 0에서부터 창사이즈까지 내림
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#스크립트를 실행 
    time.sleep(1)
    
scroll_down(driver)

#이미지를 추출하여 저장합니다.
file_no = 0
count = 1
img_src2 = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
img_src = soup.find('div','box_txtPhoto').find_all('img')

for i in img_src:
    img_src1 = i['src']#src 속성만 가져와서 담고
    img_src2.append(img_src1)
    count += 1

for i in range(0, len(img_src2)):#저장을 반복문으로 실행
    try:
        #urlretrieve 다운로드에 쓰이는 함수(경로, 이름)
        urllib.request.urlretrieve(img_src2[i],str(file_no)+'.jpg')
    except:
        continue
    file_no += 1
    time.sleep(0.5)
    print('%s 번째 이미지 저장중입니다.========='%file_no)
    
#요약 정보를 출력합니다.
e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간

print('='*80)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%file_no)
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*80)