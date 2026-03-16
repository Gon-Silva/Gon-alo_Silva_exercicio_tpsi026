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
            print("              AVERAGE GRADE             ")
            print("========================================")

# Main Function
def main():
    clear_console()
    print_header(1)

    i = 0
    grade_total = 0

    arr_grade = []

    while i < 10:
        print(f"{Fore.MAGENTA} > {Fore.WHITE}Insert the {i + 1}º grade (0-20)")

        try:
            grade = int(input(f"{Fore.BLUE} >  {Fore.WHITE} "))

            if 0 <= grade <= 20:
                arr_grade.append(grade)
                i = i + 1
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! BETWEEN 0 - 20 ! {Fore.WHITE}")

        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")


    for i in range(10):
        grade_total = arr_grade[i] + grade_total

    average = grade_total / 10

    print(f"{Fore.MAGENTA} > {Fore.WHITE}The average grade of the class is {(Fore.GREEN) if average > 10 else (Fore.RED)}{average}{Fore.WHITE}.")

# Start the program
if __name__ == "__main__":
    main()