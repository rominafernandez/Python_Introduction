## Exercise 3 - Math operations

# Write a program that shows the use of all 7 math functions.
# It should take at least four numbers as input from the user.

nr_one = int(input("Type a number: "))
nr_two = int(input("Type a number: "))
nr_three = int(input("Type a number: "))
nr_four = int(input("Type a number: "))

print(f"{nr_one} + {nr_two} is {nr_one + nr_two}")
print(f"{nr_two} - {nr_three} is {nr_two - nr_three}")
print(f"{nr_four} times {nr_one} is {nr_four * nr_one}")
print(f"{nr_three} divided by {nr_two} is {nr_three / nr_two}")
print(f"{nr_one} integer divided by {nr_two} is {nr_one // nr_two}")
print(f"{nr_four} to the power of {nr_two} is {nr_four ** nr_two}")
print(f"The rest of {nr_three} divided by {nr_four} is {nr_three % nr_four}")

## Exercise 66 - Using shortcuts

# Adjust your program you wrote for Exercise 03 by using the different shortcuts you learned

nr_one += 6
nr_two -= 1
nr_three /= 3
nr_four *= 10

print(f"\nNow I changed your input numbers!")

print(f"{nr_one} + {nr_two} is {nr_one + nr_two}")
print(f"{nr_two} - {nr_three} is {nr_two - nr_three}")
print(f"{nr_four} times {nr_one} is {nr_four * nr_one}")
print(f"{nr_three} divided by {nr_two} is {nr_three / nr_two}")
print(f"{nr_one} integer divided by {nr_two} is {nr_one // nr_two}")
print(f"{nr_four} to the power of {nr_two} is {nr_four ** nr_two}")
print(f"The rest of {nr_three} divided by {nr_four} is {nr_three % nr_four}")
