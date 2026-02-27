import threading
import time

num = 5;
def task1():
    global num
    print("Task 1 started")
    num += 5;
    time.sleep(2)
    print("Task 1 completed",num)


def task2():
    global num
    print("Task 2 started")
    num += 5;
    time.sleep(2)
    print("Task 2 completed", num)


thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Final value of num:", num)