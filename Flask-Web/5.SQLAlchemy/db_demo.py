from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

class Config():
    '''配置参数'''
    # sqlachemy配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1:3306/db_python"
    # 设置sqlachemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy

# ihome -> ih_user数据库名缩写_表名
# tbl_user
# 创建sqlalchemy工具对象
db = SQLAlchemy(app)



class Role(db.Model):
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User", backref="role")


# 创建数据库模型类
class User(db.Model):
    '''用户表'''
    __tablename__ = "tbl_users" # 数据库表名

    id = db.Column(db.Integer, primary_key=True) # 整形的主键，默认为自增
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))







if __name__ == "__main__":

    # 清除表
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 创建对象
    role1 = Role(name='admin')
    role2 = Role(name='stuff')
    # session记录对象任务
    db.session.add(role1)
    db.session.add(role2)
    # 提交到数据库
    db.session.commit()

    us1 = User(name='wang',email='wang@163.com',password='1234',role_id=role1.id)
    us2 = User(name='liu',email='liu@163.com',password='1234',role_id=role2.id)

    us3 = User(name='zhang',email='z@163.com',password='1234',role_id=role1.id)
    us4 = User(name='chen',email='c@163.com',password='1234',role_id=role2.id)

    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()
    # app.run(debug=True)