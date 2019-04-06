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
# 转换器
# 127.0.0.1:5000/goods/123
# @app.route("/goods/<int:good_id>")
@app.route("/goods/<good_id>") # 不加转换类型，默认是普通字符串规则（除了/字符）
def goods_detail(goods_id):
    return "goods detail page %s" % goods_id

from werkzeug.routing import BaseConverter
# 1.定义自己的转换器
class RegexConverter(BaseConverter):
    '''  '''
    def __init__(self, url_map, regex):
        # 调用父类的初始化华方法
        super().__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中
        # flask会使用这个属性进行路由正则匹配
        self.regex = regex
    def to_python(self, value):
        print("to_python方法被调用")
        # value是在路径进行正则表达式匹配的时候提取的参数
        return value
    def to_url(self, value):
        '''使用url_for方法时被调用'''
        print("to_url被调用")
        # return "1234233330"
        return value
    
# 2.自定义的转换器添加到flask中
app.url_map.converters['re'] = RegexConverter


# 127.0.0.1:500/send/18182343432
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    returbn "send sms to %s" % mobile


@app.route("/index")
def index():
    # /send/18912345333
    url = url_for("send_sms", mobile="1892345333")
    return redirect(url)


if __name__ == "__main__":
    # 通过url_map查看flask中路由信息
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # http://127.0.0.1:5000/