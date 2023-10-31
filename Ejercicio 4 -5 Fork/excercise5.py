import os
import time
import sys
import argparse

def child_process():
    print("Hi, I'm the child, PID", os.getpid(), "my parent is", os.getppid())
    time.sleep(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int, required=True)
    args = parser.parse_args()
    
    child_processes = []

    for i in range(args.number):
        child_pid = os.fork()
        if child_pid == 0:
            child_process()
            sys.exit(0)
        else:
            child_processes.append(child_pid)

    for pid in child_processes:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()