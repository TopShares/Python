from flask imprt Flask, request, abort, Resopnse

app = Flask(__name__)

@app.route("/index")
def index():
    # 1.使用元组, 返回自定义的响应信息
    #       响应体,      状态码, 响应头
    # reutrn "index page", 400, [("Study", "python"), ("city","shanghai")]
    
    # reutrn "index page", 666, {"it":"python","city","nanjing"}}
    
    # 2.使用make_reponse 构造响应信息
    import make_response
    resp = make_response("index page 2")
    resp.status = "666 python"
    resp.headers['city'] = "beijing"
    return resp

if __name__ == "__main__":
    app.run(debug=True)