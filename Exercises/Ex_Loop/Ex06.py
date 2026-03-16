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
            print("       THE FIRST 10 PRIME NUMBERS       ")
            print("========================================")

# Check if the number is prime or compound
def check_prime_number(number):
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                return False
    return True

# Main Function
def main():
    clear_console()
    print_header(1)

    first_prime_number = 0
    i = 1

    while first_prime_number < 10:
        if check_prime_number(i) == True:
            print(f"{Fore.RED}{i} {Fore.WHITE}", end="")
            first_prime_number = first_prime_number + 1
        i = i + 1

# Start the program
if __name__ == "__main__":
    main()