import os
import platform

# This function clean the console
# For this, I need to import modules like « os » and « platform »

    # os permit to interact with operating system
    # platform permit the program to understand what type of operating system the user is using

import readchar # Import the readchar library, this library only read a single char and keystrokes
from colorama import Fore, Back, Style # Import the colorama library

    # To use the readchar and colorama, it will be necessary use this command in command line

    # Before for you install this library I recommend upgrade python and install pip

    # Windows -> python -m pip install –upgrade python
    # Linux & MacOS -> pip install –upgrade python

    # readchar -> pip3 install readchar
    # colorama -> pip3 install reacolorama

import math

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function to print a header
def print_header(choice):
    match choice:
        case 1:
            print("============================================")
            print("                FINAL TEST 02               ")
            print("============================================")
        case 2:
            print("============================================")
            print("               ADD A CUSTOMER               ")
            print("============================================")
        case 3:
            print("============================================")
            print("              LIST THE CLIENTS              ")
            print("============================================")
        case 4:
            print("============================================")
            print("              SEARCH FOR CLIENTS            ")
            print("============================================")

def discount(purchase):
    if purchase < 100:
        return 0
    elif purchase < 200:
        return 0.05
    elif purchase < 500:
        return 0.10
    else:
        return 0.15
        
# Show the label
def label(id_numbers, choice, data_base):
    # Internal width of the frame
    width = 23 

    match choice:
        case 1:
            label_id = f"CLIENT {id_numbers}"
        case 2:
            label_id = f"CLIENT {data_base[id_numbers - 1]['id']}"
        case 3:
            label_id = f"PURCHASE {id_numbers}"

    print(f"+{'=' * (width + 2)}+")
    print(f"| {Fore.GREEN}{label_id.center(width)}{Fore.RESET} |")
    print(f"+{'=' * (width + 2)}+")

# Show the information of the customer
def show_information(client_data_base, id_number):
    label_name = f"{client_data_base[id_number - 1]['name']}"
    label_address = f"{client_data_base[id_number - 1]['address']}"
    label_phone = f"{client_data_base[id_number - 1]['phone']}"
    label_nif = f"{client_data_base[id_number - 1]['NIF']}"
    label_purchase = f"{client_data_base[id_number - 1]['purchase']}"
    label_discount = f"{client_data_base[id_number - 1]['discount']}"
    label_final_balance = f"{client_data_base[id_number - 1]['final balance']}"

    label(id_number, 2, client_data_base)

    print(f"\n{Fore.MAGENTA}  > {Fore.RESET}Name: {Fore.BLUE}{label_name}{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}Address: {Fore.BLUE}{label_address}{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}Phone: {Fore.BLUE}{label_phone}{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}NIF: {Fore.BLUE}{label_nif}{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}Purchase: {Fore.BLUE}{label_purchase}€{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}Discount: {Fore.BLUE}{label_discount}%{Fore.RESET}")
    print(f"{Fore.MAGENTA}  > {Fore.RESET}Final Balance: {Fore.BLUE}{label_final_balance}€{Fore.RESET}")

# Function for adding customers
def add_customer(client_data_base, numbers_of_customers):
    # ID of client number
    id_number = 1

    for i in range(numbers_of_customers):
        clear_console()

        label(id_number, 1, 0)

        name = input(f"{Fore.BLUE}  > {Fore.RESET}Client Name{Fore.BLUE} > {Fore.RESET}")
        address = input(f"{Fore.BLUE}  > {Fore.RESET}Client Address{Fore.BLUE} > {Fore.RESET}")

        while True:
            try:
                phone = int(input(f"{Fore.BLUE}  > {Fore.RESET}Client Phone{Fore.BLUE} > {Fore.RESET}"))

                if(phone > 0):
                    break

                print(f"\n{Fore.MAGENTA} > {Fore.RED}! CANNOT BE NEGATIVE !{Fore.RESET}")

            except ValueError:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER !{Fore.RESET}")

        while True:
            try:
                nif = int(input(f"{Fore.BLUE}  > {Fore.RESET}Client NIF{Fore.BLUE} > {Fore.RESET}"))

                if(nif > 0):
                    break

                print(f"\n{Fore.MAGENTA} > {Fore.RED}! CANNOT BE NEGATIVE !{Fore.RESET}")

            except ValueError:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER !{Fore.RESET}")

        label(id_number, 3, 0)

        while True:
            try:
                purchase = int(input(f"{Fore.BLUE}  > {Fore.RESET}Purchase{Fore.BLUE} > {Fore.RESET}"))

                if(purchase > 0):
                    break

                print(f"\n{Fore.MAGENTA} > {Fore.RED}! HIGHER THAN 0 !{Fore.RESET}")

            except ValueError:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER !{Fore.RESET}")

        client_data_base.append({"id": id_number, "name": name, "address": address, "phone": phone, "NIF": nif, "purchase": purchase, "discount": (discount(purchase) * 100), "final balance": (purchase - (purchase * discount(purchase)))})

        clear_console()

        show_information(client_data_base, id_number)

        id_number += 1

        print(f"\n{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
        readchar.readkey()

# Menu for adding customers
def add_customer_menu(client_data_base):
    # Variable boolean to continue the loop
    can_continue = True

    while can_continue:
        clear_console()
        print_header(2)

        print(f"\n{Fore.MAGENTA} > {Fore.RESET}How many customer do you like to add {Fore.RED}[HIGHER THAN 0]{Fore.RESET}")

        try:
            # Variable for adding customers
            numbers_of_customers = int(input(f"\n{Fore.BLUE}  > {Fore.RESET}"))

            if numbers_of_customers <= 0:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! HIGHER THAN 0 !{Fore.RESET}")
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
                readchar.readkey()

            else:
                can_continue = False
                add_customer(client_data_base, numbers_of_customers)

        except ValueError:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER !{Fore.RESET}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
            readchar.readkey()

# List client(s)
def list_client(client_data_base):
    if not client_data_base:
        print(f"\n{Fore.MAGENTA} > {Fore.RED}! ADD DATA FIRST ! {Fore.RESET}")
        print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
        readchar.readkey()
        return

    id_number = 1
    for i in range(len(client_data_base)):
        clear_console()
        print_header(3)
        show_information(client_data_base, id_number)

        if i == len(client_data_base) - 1:
            print(f"\n{Fore.MAGENTA} > {Fore.YELLOW}End of database reached.{Fore.RESET}")
            readchar.readkey()
            return
        
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Do you want continue [YES or NO]")

        respond = input(f"{Fore.BLUE} >  {Fore.WHITE} ").lower()

        if respond == "yes" or respond == "y":
            id_number += 1
            continue
        elif respond == "no" or respond == "n":
            break
        else:
            print(f"{Fore.MAGENTA} > {Fore.RED} ! YES OR NO ! {Fore.WHITE}")

# Search for one client
def search_for_clients(client_data_base):
    while True:
        clear_console()
        print_header(4)

        if not client_data_base:
            print(f"\n{Fore.MAGENTA} > {Fore.RED}! ADD DATA FIRST ! {Fore.RESET}")
            print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
            readchar.readkey()
            break

        try:
            # Variable to the user to choose
            choice = int(input(f"\n{Fore.BLUE}  > {Fore.RESET}Select a id{Fore.BLUE} > {Fore.RESET}"))

            if 0 <= (choice - 1) < len(client_data_base):
                show_information(client_data_base, choice)
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
                readchar.readkey()
                break
            else:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! CHOOSE A VALID ID ! {Fore.RESET}")

        except ValueError:
                    print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.RESET}")
        
        print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
        readchar.readkey()

# Main Function
def main():
    # Variable boolean to continue the loop
    can_continue = True

    # Create a dictionary of data base of clients
    dict_data_base_cli = []

    while can_continue:
        clear_console()
        print_header(1)

        print(f"\n{Fore.YELLOW}============ MENU ============{Fore.RESET}\n")

        print(f"{Fore.MAGENTA} > {Fore.RESET} {Fore.BLUE}1{Fore.RESET} - Add a customer")
        print(f"{Fore.MAGENTA} > {Fore.RESET} {Fore.BLUE}2{Fore.RESET} - List of customers")
        print(f"{Fore.MAGENTA} > {Fore.RESET} {Fore.BLUE}3{Fore.RESET} - Search for one customers\n")

        print(f"{Fore.MAGENTA} > {Fore.RESET} {Fore.RED}4{Fore.RESET} - Leave the program")

        try:
            # Variable to the user to choose
            choice = int(input(f"\n{Fore.BLUE}  > {Fore.RESET}Select a option{Fore.BLUE} > {Fore.RESET}"))

            match choice:
                case 1:
                    add_customer_menu(dict_data_base_cli)
                case 2:
                    list_client(dict_data_base_cli)
                case 3:
                    search_for_clients(dict_data_base_cli)
                case 4:
                    print(f"\n{Fore.MAGENTA} > {Fore.RESET}Leave the program\n")
                    can_continue = False
                case _: 
                    print(f"\n{Fore.MAGENTA} > {Fore.RED} ! INVALID NUMBER ! {Fore.RESET}")
                    print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
                    readchar.readkey()

        except ValueError:
                print(f"\n{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.RESET}")
                print(f"{Fore.MAGENTA} > {Fore.GREEN}Press any key to continue...{Fore.RESET}")
                readchar.readkey()

# Start the program
if __name__ == "__main__":
    main()