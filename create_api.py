from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory sample database
items = [
    {"id": 1, "name": "Item One", "price": 10.99},
    {"id": 2, "name": "Item Two", "price": 25.50}
]

# Root Endpoint: Prevents 404 when visiting http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running. Access items at /api/items"}), 200

# GET Endpoint: Retrieve all items
# strict_slashes=False allows both /api/items and /api/items/
@app.route('/api/items', methods=['GET'], strict_slashes=False)
def get_items():
    return jsonify({"success": True, "data": items}), 200

# POST Endpoint: Create a new item
@app.route('/api/items', methods=['POST'], strict_slashes=False)
def create_item():
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"success": False, "error": "Invalid input"}), 400

    new_item = {
        "id": len(items) + 1,
        "name": data['name'],
        "price": data['price']
    }
    items.append(new_item)
    return jsonify({"success": True, "data": new_item}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)