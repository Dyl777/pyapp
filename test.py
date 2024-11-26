from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    # Run the Flask app only if not running tests
    app.run(debug=True)
