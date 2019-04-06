# coding:utf-8

from flask import Flask, request

app = Flask(__name__)

@app.route("/index", method=['GET', 'POST'])
def index():
    # request中包含前端发送过来的所有请求数据
    # form和data 提取请求体数据
    # 通过request.form直接提取请求体中的表彰格式的数据， 是一个类字典的对象
    name = request.form.get("name")
    age = request.form.get("age")
    name_li = request.form.getlist("name")
    # args用来提取url中的参数(查询字符串)
    city = request.args.get('city')
    return "hello, name=%s, age=%s, city=%s" % (name, age, city)

if if __name__ == "__main__":
    app.run(debug=True)