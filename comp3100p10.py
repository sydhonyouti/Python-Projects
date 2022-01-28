# Sydney Honyouti
# This program will add an additional function that will calculate
# the sum of the square roots from 1 to 100,000,000. Import the
# math library to access the python square root function. Spawn
# a new child process that will execute this function concurrently
# with the sum of the square and sum of the cubes from 1 to 100,000,000

import time
import multiprocessing
import os
import math


def sumofsqr(value):
    # get process id
    print("Process id sumofsqr: " + str(os.getpid()))
    # calculate sum of cubes from 1 to value - 1
    sumofsquares = 0
    for i in range(1, value + 1):
        sumofsquares += (i * i)
    print(f"Sum of Squares from 1 to {value} is {sumofsquares}")


def sumofcube(value):
    # get process id
    print("Process id sumofcube: " + str(os.getpid()))
    sumofcubes = 0
    for i in range(1, value + 1):
        sumofcubes += (i * i * i)
    print(f"Sum of Cubes from 1 to {value} is {sumofcubes}")

def sumofsqrt(value):
    # get process id
    print("Process id sumofsqrt: " + str(os.getpid()))
    sumofsqrt = 0
    for i in range(1, value + 1):
        sumofsqrt += (math.sqrt(i))
    print(f"Sum of Square Root from 1 to {value} is {sumofsqrt}")


if __name__ == "__main__":
    value = int(input("end value: "))

    # (STEP 1) create child process sumofsqr and child process sumofcube
    proc1 = multiprocessing.Process(target=sumofsqr, args=(value,))
    proc2 = multiprocessing.Process(target=sumofcube, args=(value,))
    proc3 = multiprocessing.Process(target=sumofsqrt, args=(value,))

    # get start time of experiment
    start_time = time.perf_counter()

    # start each process
    proc1.start()
    proc2.start()
    proc3.start()

    # make sure each process terminates before moving ahead in this script
    proc1.join()
    proc2.join()
    proc3.join()

    end_time = time.perf_counter()

    print(f"Child concurrent processes ran in {round(end_time - start_time, 3)} seconds(s)")


