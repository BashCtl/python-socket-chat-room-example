import threading


def function1():
    for i in range(10):
        print("ONE ")


def function2():
    for i in range(10):
        print("TWO ")


def function3():
    for i in range(10):
        print("THREE ")

# If we call these functions, we see the first function call Must complete before the next
# They are executed linearly
# function1()
# function2()
# function3()


# We can execute these functions concurrently using threads! We must have a target for a thread.
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

# t1.start()
# t2.start()
# t3.start()

# Threads can only be run once. If you want to reuse, you must redifine.
t1 = threading.Thread(target=function1)
t1.start()

# WE can pause the main program until a thread is done
t1 = threading.Thread(target=function1)
t1.start()
t1.join()  # This pauses the main program untill the thread is complete
print("Threading rules!")
