from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    data = {"message": "Test: Hello, World!"}
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post_data():
    data = request.get_json()
    response = {"received": data}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)