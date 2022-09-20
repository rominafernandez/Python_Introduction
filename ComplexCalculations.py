## Group Exercise 1 - More complex calculations

# Each group should write a program that asks the user for at
# least 10 different numbers, they have to be floating point numbers and integers.
# Run at least 35 different mathematical operations with these
# numbers, 5 for each of the seven you used in Exercise 03
# Print out the results using either f-Strings or commas in your print commands

int_one = int(input("Type an Integer: "))
int_two = int(input("Type an Integer: "))
int_three = int(input("Type an Integer: "))
int_four = int(input("Type an Integer: "))
int_five = int(input("Type an Integer: "))
fl_one = float(input("Type a Float: "))
fl_two = float(input("Type a Float: "))
fl_three = float(input("Type a Float: "))
fl_four = float(input("Type a Float: "))
fl_five = float(input("Type a Float: "))

print(f"\n1: {int_one} und {int_one} macht {int_one + int_one} widewidewitt und {int_two} macht {int_one + int_one + int_two}...\n")
print(f"2: {int_one} + {int_two} = {int_one + int_two}")
print(f"3: {int_two} - {int_three} = {int_two - int_three}")
print(f"4: {int_four} * {int_one} = {int_four * int_one}")
print(f"5: {int_three} / {int_two} = {int_three / int_two}")
print(f"6: {fl_one} // {fl_two} = {fl_one // fl_two}")
print(f"7: {int_four}^{int_two} = {int_four ** int_two}")
print(f"8: {int_three} % {int_four} = {int_three % int_four}")
print(f"9: {fl_two} - {fl_three} = {fl_two - fl_three}")
print(f"10: {int_four} * {int_one} = {int_four * int_one}")

print("\nNow I will change some input numbers:")
print(f"11: {int_one} + 2 = {int_one + 2}")
int_one += 2
print(f"12: {int_three} - 5 = {int_three - 5}")
int_three -= 5
print(f"13: {fl_five} * 5 = {fl_five * 5}")
fl_five *= 5
print(f"14: {fl_three} / 2 = {fl_three / 2}")
fl_three /= 2

print("\nBack to normal calculations with the changed numbers.\nThree caluclations per operator:")
print(f"15: {int_one} + {int_one} = {int_one + int_one}")
print(f"16: {fl_one} + {fl_two} = {fl_one + fl_two}")
print(f"17: {int_four} + {fl_five} = {int_four + fl_five}")
print(f"18: {int_three} - {int_one} = {int_three - int_one}")
print(f"19: {fl_one} - {fl_three} = {fl_one - fl_three}")
print(f"20: {int_two} - {fl_two} = {int_two - int_two}")
print(f"21: {int_five} * {int_four} = {int_five * int_four}")
print(f"22: {fl_one} * {fl_five} = {fl_one* fl_five}")
print(f"23: {int_three} * {fl_three} = {int_three * fl_three}")
print(f"24: {int_two} / {int_two} = {int_two / int_two}")
print(f"25: {fl_five} / {fl_four} = {fl_five / fl_four}")
print(f"26: {int_three} / {fl_two} = {int_three / fl_two}")
print(f"27: {fl_three} // {fl_two} = {fl_three // fl_two}")
print(f"28: {fl_five} // {int_two} = {fl_one // fl_two}")
print(f"29: {int_one} // {fl_one} = {fl_one // fl_two}")
print(f"30: {int_two}^{int_two} = {int_two ** int_two}")
print(f"31: {int_four}^{fl_two} = {int_four ** fl_two}")
print(f"32: {fl_four}^{fl_four} = {fl_four ** fl_four}")
print(f"33: {int_one} % {int_five} = {int_one % int_five}")
print(f"34: {fl_three} % {int_four} = {fl_three % int_four}")
print(f"35: {fl_five} % {fl_four} = {fl_five % fl_four}")
