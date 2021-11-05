# Sydney Honyouti

# Problem 3
# this program will demonstrate string data and interactive input
name = input("What is your name?")
name_size = len(name)
name = name.upper()
output_text = "{} is {} characters in length"
print(output_text.format(name, name_size))

# a string is basically an array of chars and immutable
text = "Python"
for i in text:
    print(i, end="")

print()

for i in range(len(text)):
    print(text[i])

a_number = int(input("Enter a number: "))
print(a_number)
a_string = str(a_number)
for i in range(len(a_string)):
    print(a_string[i], end=" ")
print()

# Program 3
# Create a string variable and store the word "Harding University"
# Print out the string in all lower case using a string method (research)
# Print out the string in reverse using a loop and output all on one line
# print out the following: "The string HARDING UNIVERSITY has 18 characters"
harding_name = "Harding University"
print(harding_name.lower())
harding_name = harding_name.lower()
for element in harding_name[::-1]:
    print(element, end="")

print()
name_size = len(harding_name)
harding_name = harding_name.upper()
output_text = "{} has {} characters"
print("The string " + output_text.format(harding_name, name_size))
