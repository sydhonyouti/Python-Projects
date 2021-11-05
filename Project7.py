# this program will create a textfile in the current working directory
# write to the file
# close the file
# open it, read it, and display it

file1 = open("p7.txt", "w")
file1.write("Sample Text from\nan input file")
file1.close()

file1 = open("p7.txt", "r")
data = file1.read()
print(data)
file1.close()

# overwrite the text in p7.txt
# Create a list variable and initialize it to the months "January", "Feburary", "March"
# write this list to p7.txt and then output it
# Research how you can output a list like a string - join()
months_list = ["January", "Feburary", "March"]
file1 = open("p7.txt", "w")
for element in months_list:
    file1.write(element + " ")
file1.close()
str1 = ' '.join(months_list)
print()
print(str1)
