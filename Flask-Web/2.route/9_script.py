from flask import Flask
from flask_script import Manager # 启动命令的管理类
# pip install Flask-Script


app = Flask(__name__)
# create Manager管理类的object
manager = Manager(app)

@app.route("index")
def index():
    return "index page"

if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理对象来启动flask
    manager.run()