<<<<<<< HEAD
import unittest
import sys
from pathlib import Path

# 将项目根目录添加到Python搜索路径
sys.path.append(str(Path(__file__).parent.parent))  # 指向flask-web-app目录
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # 创建测试客户端
        self.client = app.test_client()

    def test_hello_world(self):
        # 测试根路由
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, NEU!')

if __name__ == '__main__':
    unittest.main()
=======
﻿import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_hello(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data == b"Hello, CI/CD with Jenkins!"
>>>>>>> d09ee7e (Initial commit with CI/CD configuration)
