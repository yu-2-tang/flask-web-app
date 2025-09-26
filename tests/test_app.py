import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
