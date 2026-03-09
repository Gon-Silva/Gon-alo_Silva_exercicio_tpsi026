# Function that check the input of the user
def check_type_data (user_input):

    # Use match to check the input of the user
    match user_input:
        case int():
            print("Integer number");
        case float():
            print("Decimal number");
        case str():
            print("Text string");
        case list():
            print("List");
        case _:
            print("Unknown type")

# Main fuction
def main():
    user_input = input("\nEnter one type of data: ")
    check_type_data(user_input)

    # Since the input will only return a string, 
    # it will be necessary to transform the input into other formats.

# Start the program
if __name__ == "__main__":
    main()