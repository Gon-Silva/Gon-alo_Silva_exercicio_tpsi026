# List of Integer

numbers = [1, 2, 3, 4, 5]

# This part of code will display the number
for number in numbers:
    print(number)

# This part of code will change the position 2 to 6
#  before -> numbers[2] = 3;
numbers[2] = 6
# after -> numbers[2] = 6;

# List of Strings

names = ["João", "Pedro", "Antonio"]
# index    0        1         2

# This part of code will display the names
for name in names:
    print(name)

print("Hello", "world", end="\n\n\n", sep="        ")
print(names[0])

# Change a element
names[0] = "Tiago"
print(names[0])

# Add a new element
names.append("Manuel")
print(names[len(names) - 1])

# Remove an element
names.remove("Manuel")
print(names[len(names) - 1])