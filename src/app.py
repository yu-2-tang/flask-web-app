from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, NEU!'

if __name__ == '__main__':
    # 服务器上由 supervisor 直接用 python3 运行该文件
    app.run(host='0.0.0.0', port=5000)
