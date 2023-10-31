import os
import time

def child_process():
    for i in range(5):
        print("I'm the child, PID", os.getpid())
        time.sleep(1)
    print("PID", os.getpid(), "exiting")

def parent_process():
    global child_pid
    for i in range(2):
        print("I'm the parent, PID", os.getpid(), "my child is", child_pid)
        time.sleep(1)
    os.wait()
    print("My child process, PID", child_pid, "exited")

child_pid = os.fork()
if child_pid == 0:
    child_process()
else:
    parent_process()