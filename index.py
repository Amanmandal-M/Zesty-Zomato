from tabulate import tabulate
from getpass import getpass
from colorama import Fore, Style

# Menu dictionary containing dish information
menu = {
    "1": {"name": "Dhosa", "price": 8.99, "available": True, "quantity": 10},
    "2": {"name": "Maggie", "price": 12.99, "available": True, "quantity": 8},
    "3": {"name": "Pizza", "price": 6.99, "available": False, "quantity": 0},
    "4": {"name": "Noodles", "price": 5.99, "available": True, "quantity": 15}
}

# Menu dictionary containing dish information
orders = []

# User dictionary containing user information
users = {}


# Menu dictionary containing dish information
admin_username = "admin"
admin_password = "zomato"


# Menu dictionary containing dish information
def display_menu():
    print("\nMenu:")
    headers = ["Dish ID", "Name", "Price", "Availability", "Quantity"]
    table_data = []

    for dish_id, dish_info in menu.items():
        availability = Fore.GREEN + \
            "Available" if dish_info["quantity"] > 0 else Fore.RED + \
            "Not Available"
        table_data.append([dish_id, dish_info['name'], dish_info['price'],
                          availability + Style.RESET_ALL, dish_info['quantity']])

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


# Adds a new dish to the menu
def add_dish():
    dish_id = input("\nEnter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    available = input("Is the dish available? (yes/no): ").lower() == "yes"
    quantity = int(input("Enter the quantity: "))

    menu[dish_id] = {
        "name": dish_name,
        "price": price,
        "available": available,
        "quantity": quantity
    }
    print(f"{dish_name} added to the menu!")


# Removes a dish from the menu
def remove_dish():
    dish_id = input("\nEnter the dish ID to remove: ")
    if dish_id in menu:
        dish_name = menu[dish_id]["name"]
        del menu[dish_id]
        print(f"{dish_name} removed from the menu!")
    else:
        print("Dish not found in the menu.")


# Updates the availability and quantity of a dish
def update_dish_availability():
    dish_id = input("\nEnter the dish ID to update availability: ")
    if dish_id in menu:
        available = input("Is the dish available? (yes/no): ").lower() == "yes"
        menu[dish_id]["available"] = available
        quantity = int(input("Enter the quantity: "))
        menu[dish_id]["quantity"] = quantity
        print("Dish availability and quantity updated successfully!")
    else:
        print("Dish not found in the menu.")


# Takes an order from the user
def take_order():
    customer_name = input("\nEnter customer name: ")
    order_items = input("Enter dish IDs (comma-separated): ").split(",")
    order_status = "received"
    order_id = len(orders) + 1

    for dish_id in order_items:
        if dish_id in menu:
            dish_info = menu[dish_id]
            if not dish_info["available"]:
                print(
                    Fore.RED + f"{dish_info['name']} is not available. Order cannot be processed." + Style.RESET_ALL)
                return

            if dish_info["quantity"] <= 0:
                print(
                    Fore.RED + f"{dish_info['name']} is out of stock. Order cannot be processed." + Style.RESET_ALL)
                return

            orders.append({
                "order_id": order_id,
                "customer_name": customer_name,
                "dish_id": dish_id,
                "status": order_status
            })

            # Reduce the quantity of the ordered dish by 1
            dish_info["quantity"] -= 1
            print(
                Fore.GREEN + f"{dish_info['name']} added to the order! Order ID: {order_id}" + Style.RESET_ALL)
        else:
            print(
                Fore.RED + f"Dish with ID {dish_id} not found in the menu." + Style.RESET_ALL)
            return

    print("Order processed successfully!")


# Updates the status of an order
def update_order_status():
    order_id = int(input("\nEnterthe order ID to update status: "))
    for order in orders:
        if order["order_id"] == order_id:
            print("Current Status:", order["status"])
            new_status = input("Enter the new status: ")
            order["status"] = new_status
            print("Order status updated successfully!")
            break
    else:
        print("Order not found.")


# Updates the status of an order
def review_orders():
    print("\nOrder Review:")
    if not orders:
        print("No orders available.")
    else:
        headers = ["Order ID", "Customer", "Dish",
                   "Status", "Remaining Quantity"]
        table_data = []

        for order in orders:
            order_id = str(order['order_id'])
            customer = order['customer_name']
            dish_id = order['dish_id']
            dish = menu.get(dish_id, {}).get('name', 'Unknown')
            status = order['status']
            remaining_quantity = menu.get(dish_id, {}).get('quantity', 0)
            table_data.append(
                [order_id, customer, dish, status, remaining_quantity])

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid", colalign=("center", "center",
              "center", "center", "center"), numalign="center", stralign="center", disable_numparse=True))


# Updates the status of an order
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
            print("5. Review Orders")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                display_menu()
            elif choice == "2":
                add_dish()
            elif choice == "3":
                remove_dish()
            elif choice == "4":
                update_dish_availability()
            elif choice == "5":
                review_orders()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print(Fore.RED + "Invalid credentials. Access denied." + Style.RESET_ALL)


# Check you are already a customer or not
def check_already_customer():
    isValid = input("\nAre you a Customer?  YES/NO : ")
    if isValid == "YES":
        return user_login()
    else:
        return user_registration()


# Register a customer
def user_registration():
    print("\nUser Registration:")
    valid = input("Proceed Further? YES/NO : ")

    if valid == "NO":
        return user_login()

    name = input("Enter your name: ")
    email = input("Enter your email: ")

    if email in users:
        print("Email already registered. Please login or use a different email.")
        return user_login()
    else:
        password = getpass("Enter your password: ")
        users[email] = {
            "name": name,
            "password": password
        }
        print("Registration successful. You can now log in with your credentials.")
        return user_login()


# Login a customer
def user_login():
    print("\nUser Login:")

    valid = input("Proceed Further? YES/NO : ")

    if valid == "NO":
        return user_registration()

    email = input("Enter your email: ")
    password = getpass("Enter your password: ")

    if email in users and users[email]["password"] == password:
        print(Fore.GREEN +
              f"Welcome, {users[email]['name']}!" + Style.RESET_ALL)
        user_section(email)
    else:
        print(Fore.RED + "Invalid credentials. Access denied." + Style.RESET_ALL)
        user_login()


# Performs the actions for the user section
def user_section(email):
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
            take_order(email)
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# Main function to run the Zomato Chronicles application
def main():
    print(Fore.MAGENTA + "Zomato Chronicles: The Great Food Fiasco" + Style.RESET_ALL)

    while True:
        print("\nMenu:")
        print("1. Admin Section")
        print("2. User Section")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            admin_section()
        elif choice == "2":
            check_already_customer()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using Zomato Chronicles!")


if __name__ == "__main__":
    main()
