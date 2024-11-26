from flask import Flask, jsonify
import unittest

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check the response status code
        self.assertEqual(response.json, {'message': 'Hello level 400 FET, Quality Assurance!'})

if __name__ == '__main__':
    # Run the Flask app only if not running tests
    import sys
    if 'unittest' in sys.modules:
        unittest.main()
    else:
        app.run(debug=True)
