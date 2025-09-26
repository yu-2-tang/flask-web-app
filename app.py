from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, CI/CD with Jenkins!"

if __name__ == "__main__":
    # 本地调试使用，生产建议用 WSGI（如 gunicorn/uwsgi）
    app.run(host="0.0.0.0", port=5000)
