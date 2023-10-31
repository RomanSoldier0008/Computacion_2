import multiprocessing
import time

def worker_function(process_id, queue):
    print(f"Process {process_id}, PID: {multiprocessing.current_process().pid}")
    time.sleep(process_id)
    queue.put(multiprocessing.current_process().pid)

if __name__ == "__main__":
    num_processes = 10
    result_queue = multiprocessing.Queue()

    processes = [multiprocessing.Process(target=worker_function, args=(i, result_queue)) for i in range(1, num_processes + 1)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("Results:")
    for pid in results:
        print(pid)