import os
import signal
import multiprocessing

def handler_A(_signum, _frame):
    pass

def handler_B(_signum, _frame):
    global pipe_BC
    message = f"Message 1 (PID={os.getpid()})\n"
    pipe_BC.send(message)
    os.kill(pid_C, signal.SIGUSR1)

def handler_C(_signum, _frame):
    global pipe_BC, pipe_AC
    message = f"Message 2 (PID={os.getpid()})\n"
    pipe_BC.send(message)
    os.kill(pid_A, signal.SIGUSR2)

    pid_A = os.getpid()
    pid_B = os.fork()

    if pid_B == 0:
        signal.signal(signal.SIGUSR1, handler_B)
        pid_C = os.fork()
        if pid_C == 0:
            signal.signal(signal.SIGUSR1, handler_C)
            while True:
                signal.pause()
        else:
            while True:
                signal.pause()
    else:
        signal.signal(signal.SIGUSR1, handler_A)
        signal.signal(signal.SIGUSR2, handler_A)
        os.kill(pid_B, signal.SIGUSR1)

        while True:
            signal.pause()
            message = pipe_BC.recv()
            pipe_AC.send(message)
            signal.pause()
            message = pipe_AC.recv()
            print(f"A (PID={os.getpid()}) reading:")
            print(message)

if __name__ == "__main__":
    pipe_AB, pipe_BC = multiprocessing.Pipe()
    pipe_AC = multiprocessing.Pipe()