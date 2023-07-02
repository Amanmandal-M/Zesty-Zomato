from tabulate import tabulate
from getpass import getpass
from colorama import Fore, Style

menu = {
    "1": {"name": "Dhosa", "price": 8.99, "available": True},
    "2": {"name": "Maggie", "price": 12.99, "available": True},
    "3": {"name": "Pizza", "price": 6.99, "available": False},
    "4": {"name": "Noodles", "price": 5.99, "available": True}
}

orders = []

admin_username = "admin"
admin_password = "zomato"


def display_menu():
    print("\nMenu:")
    headers = ["Dish ID", "Name", "Price", "Availability"]
    table_data = []

    for dish_id, dish_info in menu.items():
        availability = Fore.GREEN + "Available" if dish_info["available"] else Fore.RED + "Not Available"
        table_data.append([dish_id, dish_info['name'],
                          dish_info['price'], availability + Style.RESET_ALL])

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


def add_dish():
    dish_id = input("\nEnter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    available = input("Is the dish available? (yes/no): ").lower() == "yes"

    menu[dish_id] = {
        "name": dish_name,
        "price": price,
        "available": available
    }
    print(f"{dish_name} added to the menu!")


def remove_dish():
    dish_id = input("\nEnter the dish ID to remove: ")
    if dish_id in menu:
        dish_name = menu[dish_id]["name"]
        del menu[dish_id]
        print(f"{dish_name} removed from the menu!")
    else:
        print("Dish not found in the menu.")


def update_dish_availability():
    dish_id = input("\nEnter the dish ID to update availability: ")
    if dish_id in menu:
        available = input("Is the dish available? (yes/no): ").lower() == "yes"
        menu[dish_id]["available"] = available
        print("Dish availability updated successfully!")
    else:
        print("Dish not found in the menu.")


def take_order():
    customer_name = input("\nEnter customer name: ")
    order_items = input("Enter dish IDs (comma-separated): ").split(",")
    order_status = "received"
    order_id = len(orders) + 1

    for dish_id in order_items:
        if dish_id in menu:
            if not menu[dish_id]["available"]:
                print(Fore.RED + f"{menu[dish_id]['name']} is not available. Order cannot be processed." + Style.RESET_ALL)
                return

            orders.append({
                "order_id": order_id,
                "customer_name": customer_name,
                "dish_id": dish_id,
                "status": order_status
            })
            print(Fore.GREEN + f"{menu[dish_id]['name']} added to the order! Order ID: {order_id}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Dish with ID {dish_id} not found in the menu." + Style.RESET_ALL)
            return

    print("Order processed successfully!")


def update_order_status():
    order_id = int(input("\nEnter the order ID to update status: "))
    for order in orders:
        if order["order_id"] == order_id:
            print("Current Status:", order["status"])
            new_status = input("Enter the new status: ")
            order["status"] = new_status
            print("Order status updated successfully!")
            break
    else:
        print("Order not found.")


def review_orders():
    print("\nOrder Review:")
    if not orders:
        print("No orders available.")
    for order in orders:
        print(f"Order ID: {order['order_id']}")
        print(f"Customer: {order['customer_name']}")
        print(f"Dish: {order['dish_id']}")
        print(f"Status: {order['status']}")
        print("------------------------")


def admin_section():
    print(Fore.BLUE + "\nAdmin Section" + Style.RESET_ALL)
    username = input("Enter username: ")
    
    # Password is hidden for security reasons
    password = getpass("Enter password: ")

    if username == admin_username and password == admin_password:
        print(Fore.BLUE + "\nWelcome Admin to Zomato!!" + Style.RESET_ALL)
        while True:
            print(Fore.BLUE + "\nAdmin Menu Options:" + Style.RESET_ALL)
            print("1. Display Menu")
            print("2. Add Dish to Menu")
            print("3. Remove Dish from Menu")
            print("4. Update Dish Availability")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                display_menu()
            elif choice == "2":
                add_dish()
            elif choice == "3":
                remove_dish()
            elif choice == "4":
                update_dish_availability()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print(Fore.RED + "Invalid credentials. Access denied." + Style.RESET_ALL)


def user_section():
    print(Fore.GREEN + "\nUser Section" + Style.RESET_ALL)
    while True:
        print(Fore.GREEN + "\nUser Menu Options:" + Style.RESET_ALL)
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Update Order Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            take_order()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def main_section():
    while True:
        print("\nMain Menu Options:")
        print(Fore.GREEN + "1. Admin Section" + Style.RESET_ALL)
        print(Fore.GREEN + "2. User Section" + Style.RESET_ALL)
        print(Fore.RED + "3. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            admin_section()
        elif choice == "2":
            user_section()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program.")


if __name__ == "__main__":
    main_section()