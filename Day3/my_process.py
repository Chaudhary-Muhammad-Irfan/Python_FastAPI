import multiprocessing
import time

num = 5

def task1():
    global num
    print("Task 1 started")
    num += 5
    time.sleep(2)
    print("Task 1 completed", num)

def task2():
    global num
    print("Task 2 started")
    num += 5
    time.sleep(2)
    print("Task 2 completed", num)

process1 = multiprocessing.Process(target=task1)
process2 = multiprocessing.Process(target=task2)
process1.start()
process2.start()
process1.join()
process2.join()

print("Final value of num:", num)