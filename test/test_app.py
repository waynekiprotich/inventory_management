import pytest
from unittest.mock import patch
from app import app, inventory 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_inventory_empty(client):

    inventory.clear()
    
    response = client.get('/inventory')
    assert response.status_code == 200
    assert response.json == {"inventory": []}

@patch('utils.utils.requests.get')
def test_post_create_item(mock_get, client):
    inventory.clear() 
    

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {"product_name": "Coffee Beans", "brands": "BestBrand"}
    }

    new_item = {"name": "Coffee Beans", "brand": "BestBrand", "stock": 50, "price": 12.99, "barcode": "12345"}
    
    response = client.post('/inventory', json=new_item)
    assert response.status_code == 201
    
    get_res = client.get('/inventory')
    items = get_res.json.get('inventory', [])
    assert len(items) == 1
    assert items[0]['name'] == "Coffee Beans"

@patch('utils.utils.requests.get')
def test_patch_update_item(mock_get, client):
    inventory.clear()
    
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {"product_name": "Milk", "brands": "DairyCo"}
    }


    client.post('/inventory', json={"name": "Milk", "brand": "DairyCo", "stock": 10, "price": 4.99, "barcode": "111"})
    
    get_res = client.get('/inventory')
    item_id = get_res.json['inventory'][0]['id']
    
    update_data = {"stock": 20}
    response = client.patch(f'/inventory/{item_id}', json=update_data)
    assert response.status_code == 200
    
    get_res2 = client.get('/inventory')
    assert get_res2.json['inventory'][0]['stock'] == 20

def test_delete_item(client):
    inventory.clear()

    inventory.append({"id": 99, "name": "Sugar", "brand": "Kabras", "stock": 5, "price": 2.99, "barcode": "222"})
    
    response = client.delete('/inventory/99')
    assert response.status_code == 200
    
    get_res2 = client.get('/inventory')
    assert len(get_res2.json['inventory']) == 0