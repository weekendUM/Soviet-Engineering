from multiprocessing import Process
from datetime import datetime as time

def test(start : int, end : int):
    for i in range(start, end):
        j=0
        for i in range(100):
            j += 1

if __name__ == '__main__':
    #print("hello world")

    no_processes = int(input("Insert the amount of processes you want to start(this should be the number of actual, non-virtual threads, your CPU has): "))
    size = 1000000000
    processes = []

    start = time.now()
    print(f"starting {no_processes} processes...")
    ops = size // no_processes
    l_start = 0
    for i in range(no_processes - 1):
        l_stop = l_start + ops
        processes.append(Process(target = test, args = (l_start, l_stop,)))
        l_start = l_start + ops
    processes.append(Process(target = test, args = (l_start, size,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"time elapsed with {no_processes} process(es) for {size} steps: ", time.now() - start)

