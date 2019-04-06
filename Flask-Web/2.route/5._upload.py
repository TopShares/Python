from flask import Flask, request


app = Flask(__name__)

@app.route("/upload", method['POST'])
def upload():
    fileObj = request.files.get("pic")
    if fileObj is None:
        return "未上传文件"
    
    # 将文件保存到本地
    # with open('./demo.png','wb') as f:
    #     f.write(fileObj.read())
    
    # 使用上传的文件对象保存
    fileObj.save('./demo.png')
    return "上传成功"
    