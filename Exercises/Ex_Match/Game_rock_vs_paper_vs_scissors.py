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

# Function to print a header
def print_header():
    print("========================================")
    print("        ROCK VS PAPER VS SCISSOR        ")
    print("========================================")

# Functions that check how wins or if had draw
def check_winner(player_1, player_2):
    print(" > ", end="")

    match player_1, player_2:
        case ("rock", "scissor") | ("scissor", "paper") | ("paper", "rock"):
            print("! THE PLAYER 1 WINS !")
        case ("scissor", "rock") | ("paper", "scissor") | ("rock", "paper"):
            print("! THE PLAYER 2 WINS !")
        case ("scissor", "scissor") | ("rock", "rock") | ("paper", "paper"):
            print("! DRAW !")
        case _:
            print("! INVALID INPUT !")

def main():
    clear_console()

    print_header()

    dict_plays = []

    print("\n > PLAYER 1")
    player_1 = input("  > ").lower()
    
    print("\n > PLAYER 2")
    player_2 = input("  > ").lower()

    print("")

    check_winner(player_1, player_2)

    print("")

# Start the program
if __name__ == "__main__":
    main()