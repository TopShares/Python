from flask import flask, request, abort, Response

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    name = request.form.get()
    pwd =request.form.get()
    if name == '' and pwd == '':
        return "login succes"
    else:
        # abort立即终止视图函数的执行
        # 返回给前端特定信息
        # 1.传递状态码信息, 必须是标准的http状态码
        abort(404)
        # 2.传递响应体信息
        # resp = Response("login fail")
        # abort(resp)

@app.errorhandler(404)
def handle_404_error(err):
    '''自定义处理错误方法'''
    # 这个函数的返回值是前端用户看到的最终结果
    return "出现了404错误, 错误信息%s" % err

if __name__ == "__main__":
    app.run(debug=Truecc)