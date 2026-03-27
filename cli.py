import requests
import sys

BASE_URL = "http://127.0.0.1:5000/inventory"

def print_menu():
    print("\n" + "="*30)
    print("INVENTORY MANAGEMENT CLI")
    print("="*30)
    print("1. View all inventory")
    print("2. Add new item (via Barcode)")
    print("3. Update item stock/price")
    print("4. Delete an item")
    print("5. Exit")
    print("="*30)

def view_inventory():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            items = response.json().get("inventory", [])
            if not items:
                print("\nInventory is currently empty.")
                return
            
            print("\nCURRENT INVENTORY:")
            for item in items:
                print(f"ID: {item['id']} | {item['name']} ({item['brand']}) | Stock: {item['stock']} | Price: ${item['price']}")
        else:
            print(f"\nError fetching inventory: {response.text}")
    except requests.exceptions.ConnectionError:
        print("\nError: Cannot connect to the API. Is your Flask server running?")

def add_item():
    print("\n--- Add New Item ---")
    barcode = input("Enter product barcode (e.g., 3274080005003): ")
    
    name = input("Enter product name: ")
    brand = input("Enter product brand : ")
    
    try:
        stock = int(input("Enter initial stock amount: "))
        price = float(input("Enter item price: "))
    except ValueError:
        print("\nInvalid input. Stock must be an integer and price must be a number.")
        return

    payload = {"barcode": barcode, "stock": stock, "price": price}
    if name.strip():
        payload["name"] = name.strip()
    if brand.strip():
        payload["brand"] = brand.strip()

    print("Sending data to server...")
    
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        data = response.json().get('item', {})
        print(f"\nSuccess! Added: {data.get('name')} by {data.get('brand')}")
    else:
        print(f"\nError adding item: {response.text}")

def update_item():
    print("\n--- Update Item ---")
    item_id = input("Enter the ID of the item to update: ")
    print("Leave blank if you do not want to update a specific field.")
    
    stock_input = input("Enter new stock amount: ")
    price_input = input("Enter new price: ")
    
    payload = {}
    if stock_input:
        payload['stock'] = int(stock_input)
    if price_input:
        payload['price'] = float(price_input)
        
    if not payload:
        print("\nNo updates provided.")
        return

    response = requests.patch(f"{BASE_URL}/{item_id}", json=payload)
    if response.status_code == 200:
        print("\nItem updated successfully!")
    else:
        print(f"\nError updating item: {response.json().get('error', 'Unknown error')}")

def delete_item():
    print("\n--- Delete Item ---")
    item_id = input("Enter the ID of the item to delete: ")
    
    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("\nItem deleted successfully!")
    else:
        print(f"\nError deleting item: {response.json().get('error', 'Unknown error')}")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("\nGoodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()