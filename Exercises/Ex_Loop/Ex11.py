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
            print("========================================")
            print("            TREE ON THE LEFT            ")
            print("========================================")

# Create the tree on the left
def create_tree(number):
    for i in range(1, number + 1):
        print(str(i)*i)

# Main Function
def main():
    clear_console()
    print_header(1)

    can_continue = True

    while can_continue:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Enter your number")

        try:
            number = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

            if 1 <= number:
                can_continue = False
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! HIGHER THAN 0 ! {Fore.WHITE}")

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    print()

    create_tree(number)

    print()

# Start the program
if __name__ == "__main__":
    main()