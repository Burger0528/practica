# Module responsible for registering sales and updating inventory.
from datetime import datetime

def show_sales_history(sales):
    """Displays all recorded sales."""
    if not sales:
        print("No sales recorded.")
        return

    print("\n--- SALES HISTORY ---")
    for s in sales:
        print(f"Client: {s['client']} | Product: {s['product']} | Quantity: {s['quantity']} | "
              f"Date: {s['date']} | Discount: {s['discount']}% | Total: ${s['total_paid']}")
    print("---------------------------")


def register_sale(inventory, sales):
    """Registers a sale and updates inventory stock."""
    try:
        print("\n--- REGISTER SALE ---")

        # Validate client name
        client = input("Client name: ").strip()
        if not client:
            print("❌ Client name cannot be empty.")
            return

        client_type = input("Client type (Normal / VIP): ").strip().lower()
        if client_type not in ["normal", "vip"]:
            print("❌ Invalid client type.")
            return

        # Validate product ID
        product_id_str = input("ID of the product sold: ").strip()
        if not product_id_str.isdigit():
            print("❌ Product ID must be a number.")
            return
        product_id = int(product_id_str)

        # Find product
        product = next((p for p in inventory if p["id"] == product_id), None)
        if not product:
            print("❌ Product not found.")
            return

        # Validate quantity
        quantity_str = input("Quantity: ").strip()
        if not quantity_str.isdigit():
            print("❌ Quantity must be an integer.")
            return
        quantity = int(quantity_str)

        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            return

        if quantity > product["stock"]:
            print("❌ Not enough stock.")
            return

        # Apply discount
        discount = 10 if client_type == "vip" else 0
        subtotal = product["price"] * quantity
        total_paid = subtotal - (subtotal * discount / 100)

        # Update stock
        product["stock"] -= quantity

        # Record sale
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sales.append({
            "client": client,
            "client_type": client_type,
            "product": product["name"],
            "brand": product["brand"],
            "quantity": quantity,
            "unit_price": product["price"],
            "discount": discount,
            "total_paid": total_paid,
            "date": date
        })

        print("✅ Sale registered successfully.")

    except Exception as e:
        print(f"⚠ Unexpected error: {e}")
