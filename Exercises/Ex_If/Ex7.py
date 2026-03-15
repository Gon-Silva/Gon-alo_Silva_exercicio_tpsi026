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
            print("               GRADES                   ")
            print("========================================")

# Function for calculating average
def average_grade(arr, size):
    grade = 0
    for i in range(size):
        match i:
            case 0:
                grade = grade + 2 * arr[i] / 10
            case 1:
                grade = grade + 3 * arr[i] / 10
            case 2:
                grade = grade + 5 * arr[i] / 10

    return grade

# Function for check the grade
def approval_check(grade):
    if grade >= 6:
        print(f"{Fore.MAGENTA} > {Fore.GREEN}APPROVED {Fore.WHITE}")
    else:
        print(f"{Fore.MAGENTA} > {Fore.RED}FAILED {Fore.WHITE}")

# Main Function
def main():

    arr_grade = []
    i = 0    
    clear_console()
    print_header(1)

    # Assuming arr_grade and Fore are already defined
    while i < 3:
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Insert grade #{i + 1}")
        
        try: # If a user accidentally types a letter instead of a number, your program won't crash
            grade = int(input(f"{Fore.BLUE} > {Fore.WHITE} "))
            
            if 0 <= grade <= 10:
                i = i + 1
                arr_grade.append(grade)
                print(f"{Fore.MAGENTA} > {Fore.GREEN}! ADDED SUCCESSFULLY ! {Fore.WHITE}")
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! INVALID INPUT (0-10 only) ! {Fore.WHITE}")
                
        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    grade_average = average_grade(arr_grade, len(arr_grade))

    print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Average {grade_average}")
    approval_check(grade_average)

    print(" ")

# Start the program
if __name__ == "__main__":
    main()