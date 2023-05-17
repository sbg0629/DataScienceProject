from flask import Flask, render_template, request, redirect, send_file
from crawler import book_list

db = { "student_number" : [20220001, 20221234], 
      "book_list" : {},
      "update_time" : {},
      }

app = Flask("Bookmate")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/UserData", methods=["GET", "POST"])
def inputData():
    id, pw = "", ""
    if request.method == "POST" or request.method == "GET":
        id = request.form.get("ID")
        pw = request.form.get("PASSWORD")
        id_len = len(id)
    if (id == "" or pw == "") or (id == None or pw == None) or (id_len != 8):
        return redirect("/")
    
    id, pw = int(id), str(pw)

    for student_number_list in db["student_number"]:
        if id == student_number_list:
            return f"일치 아이디: {id}, 비밀번호: {pw}, 길이: {id_len} 학번 리스트: {db['student_number']}"
        
    db["student_number"].append(id)

    user_book_list = book_list(id=id, pw=pw)
    if user_book_list == 0:
        print("웹 페이지 로딩 오류")
        return redirect("/")
        return redirect("/", page_code=0)
    
    # return f"불일치 아이디: {id}, 비밀번호: {pw}, 길이: {id_len} 학번 리스트: {db['student_number']}"
    
    return render_template("SearchResult.html", id=id)


# 이스터 에그, html 연습용
@app.route("/EarthAndMoon")
def EarthAndMoon():
    return render_template("EarthAndMoon.html")

app.run(debug=True)