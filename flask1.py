from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_items(user_id):
    return jsonify({
        "id": user_id,
        "name": "Komal",
        "email": "123@123.com"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)