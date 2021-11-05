# this program will create a directory for a user and copy
# any files from the current working directory to this one

import os
import shutil

# change current working directory
cwd = "P6Test"
os.chdir(cwd)
print(os.getcwd())

new_dir = input("Name of new directory to create (give complete pathname): ")
# make new directory
os.mkdir(new_dir)

# copy files
prompt = "What file would you like to copy from {} to {} (enter NONE to quit): ".format(cwd, new_dir)
file_to_copy = input(prompt)

while file_to_copy != "NONE":
    if os.path.isfile(file_to_copy):
        destination = new_dir
        shutil.copy(file_to_copy, destination)

    else:
        print("{} does not exist".format(file_to_copy))
    file_to_copy = input(prompt)

# Program six - finish this program by printing all the files
# in the new directory you created. Research to find a Python function
# that can return the names of the files in a directory\
print()
print("Here are the files in" + new_dir)
files = os.listdir(new_dir)
for file in files:
    print(file)
