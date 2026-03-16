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
            print("               EVEN OR ODD              ")
            print("========================================")

# Main Function
def main():
    clear_console()
    print_header(1)

    arrNumber = []

    for i in range(30):
        arrNumber.append(i + 1)

    for i in range(30):
        if arrNumber[i] % 2 == 0:
            print(f"{Fore.MAGENTA} > {Fore.WHITE}The number, {Fore.GREEN}{arrNumber[i]}{Fore.WHITE}, is even")
        else:
            print(f"{Fore.MAGENTA} > {Fore.WHITE}The number, {Fore.RED}{arrNumber[i]}{Fore.WHITE}, is odd")

# Start the program
if __name__ == "__main__":
    main()