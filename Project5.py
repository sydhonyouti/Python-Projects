# This program will display all of the environment variables on the system
# in an easy to read format. Research the OS Module documentation (or use Google)
# KEY: COMPUTERNAME => VALUE: PE-RAGSDALE-VM
# KEY: OS => VALUE: Windows_NT
# PROCESSOR_ARCHITECTURE => VALUE: AMD64
# And so on.. for every key-value pair
import os
files = os.environ

print(files)
for i in files:
    print("KEY:" + i + " => " + "Value: " + files[i])
