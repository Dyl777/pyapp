from flask import Flask, jsonify
import unittest from pytest

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance")

class TestMyApp(unitTest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.app.get('/')
        self.assertEqual(response.json, {'message': 'Hello level 400 FET, Quality Assurance!'})



if __name__ == '__main__':
   app.run(debug=True)
   unittest.main()
