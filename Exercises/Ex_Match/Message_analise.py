import re
import os
import platform

# This function clean the console
# For this, I need to import modulos like « os » and « platform »

    # os permit to interact with operating system
    # plataform permit the program to undertand what type of operating system the user is using

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Function that checks the input of the user
def message_analysis(user_input):
    # Using re.split to handle multiple delimiters (space, ?, and comma)
    # This creates a list of words and symbols
    arr_message = re.split(r'(\s|\?|,)', user_input)

    for word in arr_message:
        # Clean up whitespace and ignore empty strings
        clean_word = word.strip()
        if clean_word:
            switch_message(clean_word)

# Function with match of message analysis
def switch_message(token):
    match token:
        case "hello" | "hi":
            print("Greeting")
        case "?":
            print("Question")
        case "bye" | "goodbye":
            print("Farewell")
        case _:
            print("Generic message") 

# Function to print a header
def print_header():
    print("========================================")
    print("            MESSAGE ANALYSIS            ")
    print("========================================")

# Main function
def main():
    clear_console()

    print_header()

    print("Try the following messages:\n")
    print("  > Write a message saying « hello » or « hi »")
    print("  > Write a message with « ? »")
    print("  > Write a message saying « bye » or « goodbye »")
    print("  > Write something\n")

    user_input = input("Write here > ").lower()
    message_analysis(user_input)

# Start the program
if __name__ == "__main__":
    main()