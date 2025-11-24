# Module responsible for generating all system reports.

def top_best_selling_products(sales):
    """Returns top 3 best-selling products by total quantity."""
    count = {}

    for s in sales:
        name = s["product"]
        count[name] = count.get(name, 0) + s["quantity"]

    return sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]


def sales_by_brand(sales):
    """Groups sales by brand and sums quantities."""
    grouped = {}

    for s in sales:
        brand = s["brand"]
        grouped[brand] = grouped.get(brand, 0) + s["quantity"]

    return grouped


def calculate_revenue(sales):
    """Calculates gross and net revenue (with discount applied)."""
    gross = sum(v["quantity"] * v["unit_price"] for v in sales)
    net = sum(v["total_paid"] for v in sales)
    return gross, net


def inventory_performance(inventory, sales):
    """Returns sold quantity vs initial inventory."""
    result = []

    for product in inventory:
        sold = sum(v["quantity"] for v in sales if v["product"] == product["name"])
        initial_total = product["stock"] + sold

        percent = (sold / initial_total * 100) if initial_total > 0 else 0

        result.append({
            "product": product["name"],
            "sold": sold,
            "initial_inventory": initial_total,
            "performance": round(percent, 2)
        })

    return result


def generate_reports(inventory, sales):
    """Prints all system reports."""
    print("\n=== SYSTEM REPORTS ===")

    # Top 3 products
    top = top_best_selling_products(sales)
    print("\n--- Top 3 Best-Selling Products ---")
    if top:
        for name, qty in top:
            print(f"{name}: {qty} units")
    else:
        print("No sales recorded.")

    # Sales by brand
    print("\n--- Sales by Brand ---")
    brands = sales_by_brand(sales)
    if brands:
        for brand, qty in brands.items():
            print(f"{brand}: {qty} units")
    else:
        print("No sales recorded.")

    # Revenue
    print("\n--- Revenue ---")
    gross, net = calculate_revenue(sales)
    print(f"Gross revenue: ${gross}")
    print(f"Net revenue:   ${net}")

    # Inventory performance
    print("\n--- Inventory Performance ---")
    perf = inventory_performance(inventory, sales)
    for r in perf:
        print(f"{r['product']} | Sold: {r['sold']} | Initial inventory: {r['initial_inventory']} | "
              f"Performance: {r['performance']}%")

    print("\n==============================")
