## Exercise 2 - Inputting

# Try to write a new Program that takes at least four different inputs.
# Two of these inputs should be numbers.
# Print out the handed over string variables.
# Let the program do at least two different mathematical
# operations (+ or – or * or /) with the numbers and print out the results of these operations.

fav_nr = int(input("Type in your favorite number: "))
rand_nr = int(input("Please type in a random int number: "))
name = input("What is your name?\n")
hobby = input("What is your favorite Hobby?\n")

print(f"\nHello {name}, it is nice to meet you")
print(f"I heard your Hobby is {hobby}... Disgusting")
print(f"\nYour favorit number is {fav_nr}. Multiplicated by {rand_nr} you get {fav_nr*rand_nr}.\n{fav_nr} + {rand_nr} is {fav_nr+rand_nr}")
