from flask impor flask
# session 会话机制,存放状态信息
app = Flask(__name__)

# flask的session需要用的密钥字符串
app.config["SECRET_KEY"] = "ak23ikdci3dsd"

# flask默认把session保存到cookie

@app.route("/login")
def login():
    # 设置session数据
    session['name'] = 'python'
    session['mobile'] = '12345'
    reutnr 'login sucess'

@app.route('/index')
def index():
    # 获取session数据
    return "hello %s" % session.get("name")
    


if __name__ == "__main__":
    app.run(debug=True)