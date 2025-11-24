# Module for managing the inventory: add, edit, delete, and show products.

def show_inventory(inventory):
    """Displays all products in the inventory."""
    if not inventory:
        print("No products in inventory.")
        return

    print("\n--- INVENTORY ---")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | Brand: {product['brand']} | "
              f"Category: {product['category']} | Price: {product['price']} | "
              f"Stock: {product['stock']} | Warranty: {product['warranty']} months")
    print("-------------------")


def add_product(inventory):
    """Adds a new product to the inventory with empty field validation."""
    print("\n--- ADD PRODUCT ---")

    try:
        def ask_field(message):
            value = ""
            while not value.strip():
                value = input(message).strip()
                if not value:
                    print("⚠ This field cannot be empty.")
            return value

        new_id = len(inventory) + 1
        name = ask_field("Product name: ")
        brand = ask_field("Brand: ")
        category = ask_field("Category: ")

        while True:
            try:
                price = float(input("Unit price: "))
                break
            except ValueError:
                print("⚠ Enter a valid price.")

        while True:
            try:
                stock = int(input("Stock quantity: "))
                break
            except ValueError:
                print("⚠ Enter a valid quantity.")

        while True:
            try:
                warranty = int(input("Warranty (months): "))
                break
            except ValueError:
                print("⚠ Enter a valid number.")

        inventory.append({
            "id": new_id,
            "name": name,
            "brand": brand,
            "category": category,
            "price": price,
            "stock": stock,
            "warranty": warranty
        })

        print("✅ Product added successfully.")

    except Exception:
        print("⚠ Unexpected error.")


def edit_product(inventory):
    """Allows modification of an existing product."""
    try:
        product_id = int(input("\nID of product to edit: "))
        product = next((p for p in inventory if p["id"] == product_id), None)

        if not product:
            print("Product not found.")
            return

        print("Press ENTER to keep the current value.\n")

        new_name = input(f"Name ({product['name']}): ") or product['name']
        new_brand = input(f"Brand ({product['brand']}): ") or product['brand']
        new_category = input(f"Category ({product['category']}): ") or product['category']

        new_price = input(f"Price ({product['price']}): ")
        new_price = float(new_price) if new_price else product['price']

        new_stock = input(f"Stock ({product['stock']}): ")
        new_stock = int(new_stock) if new_stock else product['stock']

        new_warranty = input(f"Warranty months ({product['warranty']}): ")
        new_warranty = int(new_warranty) if new_warranty else product['warranty']

        product.update({
            "name": new_name,
            "brand": new_brand,
            "category": new_category,
            "price": new_price,
            "stock": new_stock,
            "warranty": new_warranty
        })

        print("✅ Product updated successfully.")

    except ValueError:
        print("Error: invalid values.")


def delete_product(inventory):
    """Deletes a product from the inventory."""
    try:
        product_id = int(input("\nID of product to delete: "))
        product = next((p for p in inventory if p["id"] == product_id), None)

        if not product:
            print("Product not found.")
            return

        inventory.remove(product)
        print("✅ Product deleted successfully.")

    except ValueError:
        print("Error: enter a valid ID.")
