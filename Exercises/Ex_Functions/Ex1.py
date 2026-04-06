import subprocess
import os
import readchar
from colorama import Fore, Back, Style

# To use the readchar and colorama, it will be necessary use this command in command line

    # Before for you install this library I recommend upgrade python and install pip

    # Windows -> python -m pip install –upgrade python
    # Linux & MacOS -> pip install –upgrade python

    # readchar -> pip3 install readchar
    # colorama -> pip3 install reacolorama

# Function to clean the console
def clear_console():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell=True)

def break_point():
    print(f"\n{Fore.MAGENTA} > {Fore.CYAN}{Style.BRIGHT}Press any key to continue...{Style.RESET_ALL}{Fore.RESET}")
    readchar.readkey()

def print_message(message):
    print(f"\n{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")

def input_message(message:str):
    return input(f"\n{Fore.MAGENTA} > {Fore.GREEN}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.MAGENTA} > {Fore.RESET}")

def notify_invalid_selection(message:str):
    print(f"\n{Fore.MAGENTA} > {Fore.RED}{Style.BRIGHT}{message}{Style.RESET_ALL}{Fore.RESET}")
    break_point()

def is_alpha_space(string:str):
    return all(char.isalpha() or char.isspace() for char in string)

def check_uppercase(string:str):
    chars = string.split()
    for char in chars:
        for i in range(1, len(char)):
            if char[i].isupper():
                return False
    return True

def is_not_empty(string:str):
    return string.split()

def check_input(message:str):
        
    user_input = str(input_message(message))

    if not (is_alpha_space(user_input) and check_uppercase(user_input) and is_not_empty(user_input)):
        notify_invalid_selection("! INVALID NAME: contains invalid characters !")
        return True
    else:
        print_message("Valid name")
        return False

def main():

    can_continue = True

    while can_continue:

        clear_console()

        can_continue = check_input("Enter a name to validate")

if __name__ == "__main__":
    main()