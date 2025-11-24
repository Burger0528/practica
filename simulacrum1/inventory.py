# Module for product inventory management
from data import inventory

def add_product():
    try:
        print("\n--- Add Product ---")

        product_id = input("Enter product ID: ").strip()
        if not product_id.isdigit():
            print("❌ Product ID must be a number.")
            return

        product_id = int(product_id)

        if product_id in inventory:
            print("❌ A product with this ID already exists.")
            return

        name = input("Enter product name: ").strip()
        brand = input("Enter brand name: ").strip()

        quantity = input("Enter quantity: ").strip()
        if not quantity.isdigit():
            print("❌ Quantity must be a whole number.")
            return

        price = input("Enter unit price: ").strip()
        if not price.isdigit():
            print("❌ Price must be a whole number.")
            return

        inventory[product_id] = {
            "name": name,
            "brand": brand,
            "quantity": int(quantity),
            "price": int(price)
        }

        print(f"✅ Product added: {name}")

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def show_inventory():
    if not inventory:
        print("No products in inventory.")
        return

    print("\n--- Inventory ---")
    for pid, p in inventory.items():
        print(f"ID: {pid} | Name: {p['name']} | Brand: {p['brand']} | "
              f"Quantity: {p['quantity']} | Price: ${p['price']}")
    print("-----------------------")
