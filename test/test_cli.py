import sys
from io import StringIO
from unittest.mock import patch
import cli 

def test_print_menu():
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        cli.print_menu()
        printed_text = fake_out.getvalue()
        assert "INVENTORY MANAGEMENT CLI" in printed_text
        assert "1. View all inventory" in printed_text

@patch('cli.requests.get')
def test_view_inventory_cli(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "inventory": [{
            "id": 1, 
            "name": "Smocha", 
            "brand": "Kibanda", 
            "stock": 10, 
            "price": 1.99, 
            "barcode": "111"
        }]
    }
    
    with patch('sys.stdout', new_callable=StringIO) as fake_out:
        cli.view_inventory()
        printed_text = fake_out.getvalue()
        
        mock_get.assert_called_once()
        assert "Smocha" in printed_text
        assert "10" in printed_text