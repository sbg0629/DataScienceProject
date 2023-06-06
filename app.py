from flask import Flask, render_template, request, redirect

from crawler import book_list
from algorithm_test import recommand
from DataProcessing import sha512_hash, listTostr, strTolist, now_time, generate_random_number

import sqlite3
import time

# 페이지 이름 설정
app = Flask("Bookmate")

# 메인 페이지(홈 페이지) 라우팅/ 리퀘스트 방법 GET, POST
@app.route("/", methods=["GET"])
def home():
    # 사용자에게 home.html 파일을 보여줌
    return render_template("Home.html")

# "기본 페이지 URL + /UserData" 라우팅
@app.route("/UserData", methods=["POST"])
def inputData():
    start_time = time.time()
    id, pw = "", ""
    if request.method == "POST":
        # 사용자가 입력한 데이터를 받아옴
        id = request.form.get("ID")
        pw = request.form.get("PASSWORD")

    # 사용자가 입력한 데이터가 없거나, 학번이 8자리가 아니면 홈으로 리다이렉트
    if (id == "" or pw == "") or (id == None or pw == None) or (len(id) != 8):
        return redirect("/")

    # 사용자가 입력한 데이터를 데이터베이스에 저장하기 위한 형변환
    id, pw = int(id), str(pw)

    # 데이터베이스에 학번에 있는지 확인

    # 데이터베이스에 학번 추가 후, 해당 학번의 대출 리스트를 크롤링
    user_book_list = book_list(id=id, pw=pw, ReturnData=3)

    # 크롤링에 실패하면 홈으로 리다이렉트(크롤러는 작동 중 오류가 발생하면 0을 리턴)
    if user_book_list == 0:
        print("웹 페이지 로딩 오류")
        # 문제가 발생하면 홈으로 리다이렉트
        return redirect("/")
    elif user_book_list == 1:
        print("대출 기록이 없습니다.")
        return redirect("/")
    
    # 데이터베이스에 학번이 없으면 데이터베이스에 학번 추가
    else:
        re_books = recommand([item[0] for item in user_book_list])
        
    print("총 걸린 시간: {:.2f}초\n".format(time.time() - start_time))
    # 코드가 정상적으로 작동하면 SearchResult.html 페이지에 책 리스트 출력
    return render_template("SearchResult.html", bookinfos=user_book_list, student_number=id, re_books=re_books)
    return render_template("SearchResult.html", bookinfos=db_dic["Students"][id], student_number=id, re_books=db_dic[db_dic["Students"][id]])


# 이스터 에그, html 연습용
@app.route("/EarthAndMoon")
def EarthAndMoon():
    return render_template("EarthAndMoon.html")

# debug 모드로 실행
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")