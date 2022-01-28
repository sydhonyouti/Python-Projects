# Sydney Honyouti: Python Project 3
import os

cwd = 'c:\PyRoot'
os.chdir(cwd)
print(os.getcwd())
print()

for (root, dirs, files) in os.walk(cwd, topdown=True):
    print("Directory: " + root)

    #dirs is in a list; need to output the list
    if not dirs:
       print("Sub-Directories: ")
    else:
        print("Sub-Directories: ", end="")
        for i in range(len(dirs)):
            print(dirs[i] + " ", end="")
        print()

    if not files:
        print("Files: ")
    else:
        print("Files: ", end="")
        for i in range(len(files)):
            print(files[i] + " ", end="")
        print()

    print('--------------------------------')
