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
        grade = grade + arr[i]

    return grade / size

# Function for check the grade
def approval_check(arr, size, average):
    equal_average = 0
    higher_average = 0
    lowest_average = 0

    for i in range(size):
        if average == arr[i]:
            equal_average = equal_average + 1
        elif average < arr[i]:
            higher_average = higher_average + 1
        else:
            lowest_average = lowest_average + 1

    print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Grades equal to the average {equal_average}")
    print(f"{Fore.MAGENTA} > {Fore.WHITE}Grades higher to the average {higher_average}")
    print(f"{Fore.MAGENTA} > {Fore.WHITE}Grades lowest to the average {lowest_average}")

# Main Function
def main():

    arr_grade = []
    i = 0    
    clear_console()
    print_header(1)

    # Assuming arr_grade and Fore are already defined
    while i < 10:
        print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Insert grade #{i + 1}")
        
        try: # If a user accidentally types a letter instead of a number, your program won't crash
            grade = float(input(f"{Fore.BLUE} > {Fore.WHITE} "))
            
            if 0 <= grade <= 20:
                i = i + 1
                arr_grade.append(grade)
                print(f"{Fore.MAGENTA} > {Fore.GREEN}! ADDED SUCCESSFULLY ! {Fore.WHITE}")
            else:
                print(f"{Fore.MAGENTA} > {Fore.RED}! INVALID INPUT (0-20 only) ! {Fore.WHITE}")
                
        except ValueError:
            print(f"{Fore.MAGENTA} > {Fore.RED}! PLEASE ENTER A NUMBER ! {Fore.WHITE}")

    size = len(arr_grade)

    grade_average = average_grade(arr_grade, size)

    print(f"\n{Fore.MAGENTA} > {Fore.WHITE}Average: {grade_average}")
    approval_check(arr_grade, size, grade_average)

    print(" ")

# Start the program
if __name__ == "__main__":
    main()