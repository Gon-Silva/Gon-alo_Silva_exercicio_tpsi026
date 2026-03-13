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
    print("           OPERATIONS MATHS             ")
    print("========================================")

# Function to validate user input and calculate the account if the input is right
def operation(operator, num_1, num_2):

    print(" > ", end="")

    match operator:
        case "sum" | '+':
            print(f"The account of sum is {num_1 + num_2}")
        case "subtraction" | '-':
            print(f"The account of subtraction is {num_1 - num_2}")
        case "multiplication" | 'x':
            print(f"The account of multiplication is {num_1 * num_2}")
        case "devide" | '/':
            if (num_1 == 0 and num_2 == 0):
                print("! RESULT UNDEFINED !")
            elif (num_2 == 0):
                print("! CAN'T DIVIDE BY 0 !")
            else:
                print(f"The account of devide is {num_1 / num_2}")
        case _:
            print("! INVALID OPERATOR !")


# Main function
def main():
    clear_console()

    print_header()

    # Variable declaration for user input
    input_operation = ""
    inpput_number_1 = 0
    inpput_number_2 = 0

    print("\n > Sum or (+)")
    print(" > Subtraction or (-)")
    print(" > Multiplication or (x)")
    print(" > Devide or (/)\n")

    input_operation = input("  > ").lower()

    print("\n > Insert the fist number")
    inpput_number_1 = int(input("  > "))

    print("\n > Insert the second number")
    inpput_number_2 = int(input("  > "))

    print(" > ")

    operation(input_operation, inpput_number_1, inpput_number_2)


# Start the program
if __name__ == "__main__":
    main()