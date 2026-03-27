from flask import Flask, jsonify, request
from utils.utils import fetch_product_by_barcode

app = Flask(__name__)

inventory = []
next_id = 1

# GET ALL ITEMS
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify({"inventory": inventory}), 200

# ADD ITEM
@app.route('/inventory', methods=['POST'])
def add_item():
    global next_id
    data = request.get_json()
    
    barcode = data.get('barcode')
    stock = data.get('stock', 0)
    price = data.get('price', 0.0)
    
    if not barcode:
        return jsonify({"error": "Barcode is required"}), 400
   # Fetching details from External API
    api_data = fetch_product_by_barcode(barcode)

    if api_data:
        name = api_data.get('name', 'Unknown')
        brand = api_data.get('brand', 'Unknown')
    else:
        name = data.get('name', 'Unknown')
        brand = data.get('brand', 'Unknown')

    new_item = {
        "id": next_id,
        "barcode": barcode,
        "name": name,
        "brand": brand,
        "stock": stock,
        "price": price
    }

    inventory.append(new_item)
    next_id += 1
    return jsonify({"message": "Item added successfully", "item": new_item}), 201

# Get one item
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Fetch a single item by its ID."""
    item = next((i for i in inventory if i['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404

# Get one item
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    
    item = next((i for i in inventory if i['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    
    
    if 'stock' in data:
        item['stock'] = data['stock']
    if 'price' in data:
        item['price'] = data['price']
        
    return jsonify({"message": "Item updated successfully", "item": item}), 200

# Get one item
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):

    global inventory
    initial_length = len(inventory)
    

    inventory = [i for i in inventory if i['id'] != item_id]
    
    if len(inventory) < initial_length:
        return jsonify({"message": "Item deleted successfully"}), 200
        
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

