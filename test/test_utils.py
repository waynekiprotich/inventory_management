from unittest.mock import patch
from utils.utils import fetch_product_by_barcode

@patch('utils.utils.requests.get')
def test_fetch_external_api_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Mock Mocha",
            "brands": "MockBrand"
        }
    }

    result = fetch_product_by_barcode("123456789")
    
    assert result is not None
    assert "Test Mock Mocha" in str(result)

@patch('utils.utils.requests.get')
def test_fetch_external_api_not_found(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 0,
        "status_verbose": "product not found"
    }

    result = fetch_product_by_barcode("000000000")
    
    assert result is None