# Sydney Honyouti

# Problem 2
a_number = 5
if a_number > 0:
    print(a_number * 2)
elif a_number == 0:
    print(a_number)
else:
    print(a_number * 10)

# This program will demonstrate looping (iteration) structure - for
max_value = 4
for i in range(max_value):
    print(i, end=" ")  # This will print the numbers out in the same line - putting end=" "

# Program two - comp3100.py
# Put your name in a comment at the top for this for all programs submitted to CANVAS
# Create a string variable called PYTHON and loop through each character
# If the ascii value of the character is even then write "EVEN"
# If odd, then output "ODD"
# The output should look like this:
# P is the ascii 80 - EVEN
# Y is the ascii 89 - ODD
# and so forth
print()

pyString = 'PYTHON'
for element in pyString:
    if ord(element) % 2 == 0:
        print(element + " is the ascii " + str(ord(element)) + " - EVEN")
    elif ord(element) % 2 != 0:
        print(element + " is the ascii " + str(ord(element)) + " - ODD")
