from flask import Flask, request, render_template

# Flask 애플리케이션 생성
app = Flask(__name__)

# GET 요청 처리
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # HTML 파일 렌더링

# POST 요청 처리
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")  # 폼 데이터에서 'name' 가져오기
    if name:
        return render_template("greet.html", name=name)  # 이름과 함께 HTML 렌더링
    else:
        return render_template("error.html")  # 이름이 비어 있는 경우 에러 페이지 렌더링

# 서버 실행
if __name__ == "__main__":
    print("서버를 실행 중입니다... http://127.0.0.1:5000 에 접속하세요!")
    app.run(debug=True)
