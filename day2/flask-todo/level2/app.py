from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 세션 관리를 위한 자동생성 비밀키 설정 (보안)

# 각 사용자의 할 일 목록을 저장할 딕셔너리
todos = {}

# 기본 페이지 (GET 방식)
@app.route('/')
def index():
    # 로그인하지 않은 경우 로그인 페이지로 이동
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # 로그인한 사용자의 할 일 목록 표시
    user_todos = todos.get(session['username'], [])
    return render_template('todos.html', 
                         username=session['username'],
                         todos=user_todos)

# 로그인 페이지 (GET, POST 방식 모두 처리)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # POST: 로그인 폼 제출 처리
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    
    # GET: 로그인 페이지 표시
    return render_template('login.html')

# 새로운 할 일 추가 (POST 방식)
@app.route('/add', methods=['POST'])
def add_todo():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    new_todo = request.form['todo']
    if new_todo:  # 빈 내용이 아닌 경우에만 추가
        if session['username'] not in todos:
            todos[session['username']] = []
        todos[session['username']].append(new_todo)
    
    return redirect(url_for('index'))

# 할 일 삭제 (GET 방식)
@app.route('/delete/<int:index>')
def delete_todo(index):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_todos = todos.get(session['username'], [])
    if 0 <= index < len(user_todos):
        user_todos.pop(index)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)