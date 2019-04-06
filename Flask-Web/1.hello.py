'''
Flask 基于Werkzeug工具箱编写的轻量级Web开发框架
Flask框架的核心:Werkzeug和Jinja2(模板)
'''

from flask import Flask, current_app

# flask 以这个模块所在的目录为总目录,  默认目录中static为表态目录，templates为模板目录
app = Flask(__name__,   # 当前的模块名字
            static_url_path="/python", #访问表态资源url前缀，默认值为static
            static_folder="static",    #静态文件的目录，默认static
            template_folder='templates', #模板文件的目录，默认templates
            ) 
# 配置参数的使用方式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用对象配置参数
class Config(object):
    # 字典
    DEBUG = True
    STUDY = 'python'
app.config.from_object(Config)

# 3.直接操作config的字典对象
# app.config["DEBUG"] = True

@app.route("/")
def index():
    '''定义视图函数'''
    # 读取配置参数
    # 1.直接从全局对象app的config字典中取
    # app.config.get('STUDY')
    # 2.通过current_app取值
    current_app.config.get('STUDY')

    return "hello flask"

if __name__ == "__main__":
    # app.run()       # start flask app
    # app.run(host='192.168.1.12', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # http://127.0.0.1:5000/