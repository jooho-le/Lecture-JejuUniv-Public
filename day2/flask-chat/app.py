# app.py
from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit
import secrets

# Flask 애플리케이션 초기화
app = Flask(__name__)
# 세션 관리를 위한 자동생성 비밀키 설정 (보안)
app.config['SECRET_KEY'] = secrets.token_hex(16)
# SocketIO 초기화 - WebSocket 기능 추가
socketio = SocketIO(app)

# 채팅 메시지를 저장할 리스트 (실제 서비스에서는 데이터베이스 사용 권장)
messages = []

# 메인 페이지 라우트
@app.route('/')
def index():
    # 로그인하지 않은 사용자는 로그인 페이지로 리다이렉트
    if 'username' not in session:
        return redirect(url_for('login'))
    # 로그인된 사용자에게 채팅 페이지 표시
    return render_template('chat.html', messages=messages)

# 로그인 페이지 라우트
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # POST 요청일 경우 사용자 이름을 세션에 저장
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    # GET 요청일 경우 로그인 페이지 표시
    return render_template('login.html')

# WebSocket 메시지 수신 이벤트 핸들러
@socketio.on('message')
def handle_message(data):
    # 새 메시지 구성
    message = {
        'user': session['username'],
        'message': data['message']
    }
    # 메시지 저장
    messages.append(message)
    # 모든 클라이언트에게 메시지 브로드캐스트
    emit('message', message, broadcast=True)

# 애플리케이션 실행
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)