import os
import platform

# Function to clean the console
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def swap(number_1, number_2):
    number_1, number_2 = number_2, number_1

    return number_1, number_2

def insert_value(array):
    array.append(19)

def main():
    
    number_1 = 12
    number_2 = 13

    array = [12, 13, 14]

    clear_console()

    print("Before")
    print(f" Number 1 - {number_1}\n Number 2 - {number_2}\n")

    number_1, number_2 =swap(number_1, number_2)

    print("After")
    print(f" Number 1 - {number_1};\n Number 2 - {number_2}\n")


    print("\nBefore")
    print(f" Array {array}\n")

    insert_value(array)

    print("After")
    print(f" Array {array}\n")

if __name__ == "__main__":
    main()