from flask import Flask, make_response
'''
cookie 其是就是响应头设置为Set-Cookie : key=value
'''

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie, 默认有效期是临时cookie, 浏览器关闭时失效
    resp.set_cookie("Study","python")
    resp.set_cookie("Study2","python2")
    # max_age设置有效期, 单位：秒
    resp.set_cookie("Study3","Python3",max_age=3600)
    # 自己设置cookie
    resp.headers['Set-Cookie'] = "Study4=Python;Expires=Sat,18-Nov-2017 04:04:04 GMT; Max-Age=3600;path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    c=request.cookie("Study")
    return c

@app.route("/del_cookie")
def del_cookie():
    resp = make_response("del success")
    # 删除cookie
    # 并未真的删除cookie, 只是修改cookie有效期,只有浏览器能删除cookie
    resp.delete_cookie("Study3")
    return resp

if __name__ == "__main__":
    app.run(debug=True)