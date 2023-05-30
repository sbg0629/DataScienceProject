function check_info() {
    var id = document.getElementsByName("ID")[0].value;
    var pw = document.getElementsByName("PASSWORD")[0].value;
    // id 타입 체크하기
    if (id == "" && pw == "") {
        alert("아이디와 비밀번호를 입력하세요.");
    }
    else if (id == ""){
        alert("아이디를 입력하세요.");
    }
    else if (pw == ""){
        alert("비밀번호를 입력하세요.");
    }
    else if (id.length != 8){
        alert("학번을 아이디로 입력해주세요.")
    }
}