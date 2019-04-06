from flask import Flask,render_template

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        'name':"python",
        'age':18,
        "dic":{'city':'Tokoy'},
        'lis':[1,2,3,4,5],
        
    }
    return render_template("index.html", **data)

def list_step_2(li):
    '''自定义过滤器'''
    return li[::2]

# 注册过滤器
app.add_template_filter(list_step_2, "li2")


@app.template_filter("li3")
def list_setp_3:
    return li[::3]

if __name__ == "__main__":
    app.run(debug=True)