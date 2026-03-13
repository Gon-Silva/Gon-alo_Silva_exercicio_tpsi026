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
    print("          REQUEST PROCESSING            ")
    print("========================================")

# Function to check the request 
def request_check(request):
    print(" > ", end="") # to avoid a new line

    match request:
        case {"resquest": "GET", "content": ""}:
            print("GET request without comment")
        case {"resquest": "GET", "content": content}:
            print(f"GET request received with comment \"{content}\"")
        case {"resquest": "POST", "content": ""}:
            print(f"POST request received without comment")
        case {"resquest": "POST", "content": content}:
            print(f"POST request received with comment \"{content}\"")
        case _:
            print("! METHOD NOT SUPPORTED !")


# Main function
def main():
    clear_console()

    print_header()

    # Create a dictonary
    dict_resquest = []

    print("\n > How many request do you want insert?")
    numbers_of_input = int(input("\n  > "))

    for i in range(numbers_of_input):
        print(f"\n > Request {i + 1}")

        print("  > Insert type of request: ")
        request = input("   > ").upper()

        print("  > Insert the content of the request: ")
        content = input("   > ")

        dict_resquest.append({"resquest": request, "content": content})

    print("")

    for resquests in dict_resquest:
        request_check(resquests)

    print("")

# Start the program
if __name__ == "__main__":
    main()