import multiprocessing
import os

def reading_process(pipe):
    while True:
        message = input("Enter a message: ")
        pipe.send(message)

def display_process(pipe):
    pid = os.getpid()
    while True:
        message = pipe.recv()
        print(f"Reading (PID: {pid}): {message}")

if __name__ == "__main__":
    pipe_a, pipe_b = multiprocessing.Pipe()

    process1 = multiprocessing.Process(target=reading_process, args=(pipe_a,))
    process2 = multiprocessing.Process(target=display_process, args=(pipe_b,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()