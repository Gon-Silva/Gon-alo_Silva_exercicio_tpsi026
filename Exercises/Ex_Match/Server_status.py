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
    print("             SERVER STATUS              ")
    print("========================================")

# Function to check the server status 
def server_status(dict_status):
    match dict_status:
        # Using the `if` statement to check the data, time, and server status
            # Check the status_value is equal to "ok", and status_time is equal or less than 200ms
        case {"status": status_value, "time": status_time} if status_time <= 200 and status_value == "ok":
            print(f"Active server | Status: {status_value} | Time: {status_time}")
            # Check the status_value is equal to "ok", and status_time is higher than 200ms
        case {"status": status_value, "time": status_time} if status_time > 200 and status_value == "ok":
            print(f"Slow server   | Status: {status_value} | Time:: {status_time}")
        case _:
            print("Unknown state")

# Main function
def main():
    clear_console()

    print_header()

    # Create a dictonary
    dict_status = []

    print("\n > Insert the number of time the server respond")
    number_of_responses = int(input("\n  > "))

    for i in range(number_of_responses):
        print(f"\n > {i + 1} Respond")

        print("  > Insert the status of server > ")
        status_server = input("   > ").lower()

        print("  > Insert the time the server respond > ")
        status_time = int(input("   > "))

        dict_status.append({"status": status_server, "time": status_time})

    print("") # A space between the questions and the answers

    for respondes in dict_status:
        server_status(respondes)

    print("") # A space between the answers and the console

# Start the program
if __name__ == "__main__":
    main()
