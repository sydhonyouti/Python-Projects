# Sydney Honyouti

# Problem 4
# This program will demonstrate the list abstract data type
list1 = ['Tom', 100, "This is a sentence"]
for i in list1:
    print(i)

a_string = "Python programming is fun"
list2 = a_string.split()
print(list2)

list1 = list1 + list2
print(list1)

del list1[3]
print(list1)

# Program Four
# Create a List that contains peach, banana, pear, apple
# Add the value grape to the list
# sort the list
# print the list
fruit_list = ["peach", "banana", "pear", "apple"]
fruit_list.append("grape")
fruit_list.sort()
print(fruit_list)
