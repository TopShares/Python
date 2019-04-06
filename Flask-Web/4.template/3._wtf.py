from flask import Flask

from flask import render_template, redirect, url_for,session
app = Flask(__name__)

app.config['SECRET_KEY'] = 'shxifu23jsdiu23'
# Flask-WTF 0.14.2
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, EqualTo

#自定义表单类，文本字段、密码字段、提交按钮
class RegisterForm(FlaskForm):
    username = StringField("用户名：", [DataRequired(message='用户名不能为空')])
    password = PasswordField("密码：", [DataRequired('密码不能为空')])
    password2 = PasswordField("确认密码：", [DataRequired('密码不能为空'), EqualTo("password",'两次密码不一')])
    submit = SubmitField("注册")

@app.route("/register", methods=['GET','POST'])
def regiseter():
    # 创建表单对象, 前端发送数据, flask把数据构造from对象时，存放在对象中
    form = RegisterForm()

    # 判断form中数据是否合理
    if form.validate_on_submit():
        # 验证合格
        name = form.username.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(name,pwd,pwd2)
        session['user_name'] = name
        return redirect(url_for("index"))

    return render_template('register.html', form=form)

@app.route("/index")
def index():
    user_name = session.get('user_name','')
    # return "index page"
    return "hello %s" % user_name 
if __name__ == "__main__":
    app.run(debug=True)