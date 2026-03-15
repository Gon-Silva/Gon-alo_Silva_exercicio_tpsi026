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
            print("              CHECK MONTHS              ")
            print("========================================")

# Main Function
def main():
    clear_console()
    print_header(1)

    arr_number = []

    i = 0
    even_number = 0
    odd_number = 0

    while i < 10:
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Insert a number")
            
        try: # If a user accidentally types a letter instead of a number, your program won't crash
            number = float(input(f"{Fore.BLUE} > {Fore.WHITE} "))
                
            arr_number.append(number)
            i = i + 1
                    
        except ValueError:
                print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    for i in range(len(arr_number)):
        if arr_number[i] % 2 == 0:
            even_number = even_number + 1
        else:
            odd_number = odd_number + 1
    
    print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Even number: {even_number}")
    print(f"{Fore.MAGENTA} > {Fore.WHITE}Odd number: {odd_number}")

    print(" ")

# Start the program
if __name__ == "__main__":
    main()