import os
import platform

# This function clean the console
# For this, I need to import modulos like « os » and « platform »

    # os permit to interact with operating system
    # plataform permit the program to undertand what type of operating system the user is using

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to print a header
def print_header():
    print("========================================")
    print("           CLASSIFY PRODUCTS            ")
    print("========================================")

# Function to check the product 
def server_status(product):
    match product:
        # Using the `if` statement to check the category and price
            # Check the status_value is equal to "ok", and status_time is equal or less than 200ms
        case {"name": name, "category": category, "price": price} if price > 1000 and category == "electronic":
            print(f"Your product, {name}, is luxury electronics")
            # Check the status_value is equal to "ok", and status_time is higher than 200ms
        case {"name": name,"category": category, "price": price} if price <= 1000 and category == "electronic":
            print(f"Your product, {name}, is common electronic profuct")
        case {"name": name,"category": category, "price": price} if category == "food":
            print(f"Your product, {name}, is food product")
        case _:
            print("Unknown category")

# Main function
def main():
    clear_console()

    print_header()

    # Create a dictonary
    dict_products = []

    print("\n > How many product do you want insert?")
    numbers_of_input = int(input("\n  > "))

    for i in range(numbers_of_input):
        print(f"\n > Product {i + 1}")

        print("  > Insert the name: ")
        name_product = input("   > ").lower()

        print("  > Insert the category: ")
        category_product = input("   > ")

        print("  > Insert the price: ")
        price_product = int(input("   > "))

        dict_products.append({"name": name_product, "category": category_product, "price": price_product})

    print("") # A space between the questions and the answers

    for respondes in dict_products:
        server_status(respondes)

    print("") # A space between the answers and the console

# Start the program
if __name__ == "__main__":
    main()
