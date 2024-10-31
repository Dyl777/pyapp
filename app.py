from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample in-memory data storage
data = {}

@app.route('/api/resource', methods=['POST'])
def create_resource():
    if not request.json or 'key' not in request.json:
        abort(400)  # Bad Request if 'key' is missing in JSON data
    resource_id = len(data) + 1
    data[resource_id] = request.json
    return jsonify({"id": resource_id}), 201

@app.route('/api/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = data.get(resource_id)
    if resource is None:
        abort(404)  # Not Found
    return jsonify(resource)

if __name__ == '__main__':
    app.run(debug=True)
