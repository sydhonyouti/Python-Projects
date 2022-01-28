# Sydney Honyouti

# This script will use Python process module called psutil to
# display information about current running processes on
# my system
import psutil

for process in psutil.process_iter(['pid', 'name', 'username']):
    print(process.info)

print()
print()

# ASSIGNMENT NINE
# Display a sorted list of running processes & sorted
# Capitalize all the names and sort the processes
# Iterate over all running process

processName = []
print("SORTED RUNNING PROCESS LISTING")
print("------------------------------")
for proc in psutil.process_iter(['pid', 'name', 'username']):
    processName.append(proc.info['name'])

# Sorting the list
processName.sort()

# Making all the elements of processName uppercase
for i in range(len(processName)):
    processName[i] = processName[i].upper()

# Printing all the processes
for i in processName:
    print(i)

