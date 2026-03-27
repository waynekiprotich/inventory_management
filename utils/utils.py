import requests

def fetch_product_by_barcode(barcode):

    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
    

    headers = {
        "User-Agent": "InventoryLabApp/1.0 (waynekip123@icloud.com)" 
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data.get("status") == 1:
            product = data.get("product", {})
            return {
                "name": product.get("product_name", "Unknown Product"),
                "brand": product.get("brands", "Unknown Brand")
            }
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None