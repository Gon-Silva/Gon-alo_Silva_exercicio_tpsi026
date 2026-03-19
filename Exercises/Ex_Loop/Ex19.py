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
            print("           SUM OF FIBONACCI SERIES          ")
            print("============================================")


# Main Function
def main():
    clear_console()
    print_header(1)

    prev_num_b = 0

    num_a, num_b = 1, 1

    for i in range(1, 61):
        if i <= 2:
            print(f"{Fore.MAGENTA} > {Fore.WHITE}Fibonacci number {Fore.BLUE}{i:2}{Fore.WHITE} → {Fore.YELLOW}{num_a}{Fore.WHITE}")
        else:
            print(f"{Fore.MAGENTA} > {Fore.WHITE}Fibonacci number {Fore.BLUE}{i:2}{Fore.WHITE} → {Fore.YELLOW}{num_a}{Fore.WHITE} = {num_a - prev_num_b} + {prev_num_b}{Style.RESET_ALL}")

        prev_num_b = num_a

        num_a, num_b = num_b, num_a + num_b
        # num_a = num_b
        # num_b = num_a + num_b

# Start the program
if __name__ == "__main__":
    main()