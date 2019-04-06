from flask import flask

app = Flask(__name__)


@app.route("/index")
def index():
    # json就是字符串
    data = {
        'name': 'python',
        'age': 18,
    }
    # import json
    # # json.dumps(字典) # 将字典转换为json
    # # json.loads(字符串)  # 将字符串转换为字典
    # json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type":"application/json"}

    from flask import jsonify
    return jsonify(data)