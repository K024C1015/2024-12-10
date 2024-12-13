from flask import Flask
from flask import make_response,request # Cookieのため --- (*1)
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    cnt_s = request.cookies.get('cnt')
    last_visit = request.cookies.get('last_visit')
    if cnt_s is None:
        cnt = 0
    else:
        cnt = int(cnt_s)
    cnt += 1

    if last_visit is None:
        last_visit_message = "初めての訪問です！"
    else:
        last_visit_message = f"前回の訪問日時: {last_visit}"

    response = make_response(f"""
        <h1>訪問回数: {cnt}回</h1>
        <p>{last_visit_message}</p>
    """)
    max_age = 60 * 60 * 24 * 90  # 90日
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('cnt', value=str(cnt), max_age=max_age, expires=expires)
    response.set_cookie('last_visit', value=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), max_age=max_age, expires=expires)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

