import os
import sys
import multiprocessing

def sender(conn, message):
    to_send = message
    conn.send(to_send)
    conn.close()

def receiver(conn):
    pid = os.getpid()
    while True:
        message = conn.recv()
        print("Reading (PID={pid}): {message}".format(pid=pid, message=message))

if __name__ == "__main__":
    message = input("Enter a message: ")
    parent_conn, child_conn = multiprocessing.Pipe()
    process1 = multiprocessing.Process(target=sender, args=(child_conn, message))
    process2 = multiprocessing.Process(target=receiver, args=(parent_conn,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    sys.exit(0)