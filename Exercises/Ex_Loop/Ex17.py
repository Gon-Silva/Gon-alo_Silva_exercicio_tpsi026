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
            print("============================================")
            print("        MULTIPLES OF 5 IN 1000 NUMBERS      ")
            print("============================================")

# Check if the number is only multiple of 5
def check_only_multiple_of_5(number, arr_number):
    if number % 3 == 0:
        return
    if number % 5 == 0:
        arr_number.append(number)

# Main Function
def main():
    clear_console()
    print_header(1)

    arr_number = []
    
    for i in range(1, 1001):
        check_only_multiple_of_5(i, arr_number)

    for i in range(len(arr_number)):
        print(f"{Fore.MAGENTA} > {Fore.WHITE} Number {Fore.BLUE}{i+1}{Fore.WHITE} - {arr_number[i]}")

# Start the program
if __name__ == "__main__":
    main()