from products import add_product, show_inventory, edit_product, delete_product
from sales import register_sale, show_sales_history
from reports import generate_reports
from data import inventory, sales

def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Add Product")
        print("2. Show Inventory")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Register Sale")
        print("6. Show Sales History")
        print("7. Generate Reports")
        print("0. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            add_product(inventory)
        elif option == "2":
            show_inventory(inventory)
        elif option == "3":
            edit_product(inventory)
        elif option == "4":
            delete_product(inventory)
        elif option == "5":
            register_sale(inventory, sales)
        elif option == "6":
            show_sales_history(sales)
        elif option == "7":
            generate_reports(inventory, sales)
        elif option == "0":
            print("Exiting the system...")
            break
        else:
            print("❌ Invalid option, please try again.")


if __name__ == "__main__":
    main_menu()
#git mind
#intellcode, intellcode comple, intell code insiders, errorlens,