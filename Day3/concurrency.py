# concurrency in python. Concurrency is the ability of a program to handle multiple tasks at the same time. It does not mean they are executed at the same time. 

# we can achieve concurrency in three different ways:
# 1. Threading.
# 2. Multi-processing.
# 3. Asynchronous programming.

# threading in python. Threading is a way to achieve concurrency by creating multiple threads of execution within a single process.
# Example:
import threading
import time
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")
def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")
thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All tasks completed")
print('--------------------------------')


# multi-processing in python. Multi-processing is a way to achieve concurrency by creating multiple processes of execution within a single program.
# Example:
import multiprocessing
import time
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")
def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 completed")
process1=multiprocessing.Process(target=task1)
process2=multiprocessing.Process(target=task2)
process1.start()
process2.start()
process1.join()
process2.join()
print("All tasks completed")
print('--------------------------------')

# asynchronous programming in python. Asynchronous programming is a way to achieve concurrency by using asynchronous functions.
# Example:
import asyncio
async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")
async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

asyncio.run(task1())
asyncio.run(task2())
print("All tasks completed")