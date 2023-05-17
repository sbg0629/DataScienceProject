from flask import Flask, render_template, request, redirect
from crawler import book_list

# 데이터베이스 + 더미 데이터
db = { "student_number" : [20220001, 20221234], 
      "book_list" : {},
      "update_time" : {},
      }

# 페이지 이름 설정
app = Flask("Bookmate")

# 메인 페이지(홈 페이지) 라우팅/ 리퀘스트 방법 GET, POST
@app.route("/", methods=["GET", "POST"])
def home():
    # 사용자에게 home.html 파일을 보여줌
    return render_template("home.html")

# "기본 페이지 URL + /UserData" 라우팅
@app.route("/UserData", methods=["GET", "POST"])
def inputData():
    id, pw = "", ""
    if request.method == "POST" or request.method == "GET":
        # 사용자가 입력한 데이터를 받아옴
        id = request.form.get("ID")
        pw = request.form.get("PASSWORD")
        id_len = len(id)

    # 사용자가 입력한 데이터가 없거나, 학번이 8자리가 아니면 홈으로 리다이렉트
    if (id == "" or pw == "") or (id == None or pw == None) or (id_len != 8):
        return redirect("/")
    
    # 사용자가 입력한 데이터를 데이터베이스에 저장하기 위한 형변환
    id, pw = int(id), str(pw)

    # 데이터베이스에 학번에 있는지 확인
    for student_number_list in db["student_number"]:
        if id == student_number_list:
            # 아이디가 일치하면 단순히 아이디와 비밀번호를 출력
            return f"일치 아이디: {id}, 비밀번호: {pw}, 길이: {id_len} 학번 리스트: {db['student_number']}"
        
    # 데이터베이스에 학번이 없으면 데이터베이스에 학번 추가
    db["student_number"].append(id)

    # 데이터베이스에 학번 추가 후, 해당 학번의 대출 리스트를 크롤링
    user_book_list = book_list(id=id, pw=pw)

    # 크롤링에 실패하면 홈으로 리다이렉트(크롤러는 작동 중 오류가 발생하면 0을 리턴)
    if user_book_list == 0:
        print("웹 페이지 로딩 오류")
        return redirect("/")
        # 현재는 작동하지 않는 코드, html 파일에 page_code를 넘겨주는 방식으로 변경해야 함(문제가 발생하면 홈으로 리다이렉트하고 알람을 띄우기 위함)
        return redirect("/", page_code=0)
    
    # 코드가 정상적으로 작동하면 SearchResult.html 페이지에 책 리스트 출력
    return render_template("SearchResult.html", id=user_book_list)


# 이스터 에그, html 연습용
@app.route("/EarthAndMoon")
def EarthAndMoon():
    return render_template("EarthAndMoon.html")

# debug 모드로 실행
app.run(debug=True)