'''
Flask 基于Werkzeug工具箱编写的轻量级Web开发框架
Flask框架的核心:Werkzeug和Jinja2(模板)
'''

from flask import Flask, current_app, redirect, url_for

# flask 以这个模块所在的目录为总目录,  默认目录中static为表态目录，templates为模板目录
app = Flask(__name__,   # 当前的模块名字
            static_url_path="/python", #访问表态资源url前缀，默认值为static
            static_folder="static",    #静态文件的目录，默认static
            template_folder='templates', #模板文件的目录，默认templates
            ) 
@app.route("/")
def index():
    '''定义视图函数'''
    return "hello flask"

# 通过methods访问方式
@app.route("/post_only", methods=['POST','GET'])
def post_only():
    return "post only page"

# 两个不同视图函数使用同一个路径
@app.route("/hello"， methods=['POST'])
def hello():
    return "hello"

@app.route("/hello", methods=['GET'])
def hello2():
    return "hello2"

# 一个视图函数使用两个路径
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"

@app.route("/login")
def login():
    
    # 使用url_for, 通过视图函数名找到视图对应url
    url = url_for("index")
    return redirect(url)

def register():
    url = url_for("index")
    return redirect(url)


if __name__ == "__main__":
    # 通过url_map查看flask中路由信息
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # http://127.0.0.1:5000/