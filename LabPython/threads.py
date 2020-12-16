import threading as thr
from threading import Thread
from datetime import datetime

def run(no_threads, func, steps):
    starttime = datetime.now()
    threads = []
    l_start = 0
    ops = steps // no_threads
    for i in range(no_threads - 1):
        l_stop = l_start + ops
        threads.append(Thread(target = func, args = (i, l_start, l_stop,)))
        l_start = l_stop
    threads.append(Thread(target = func, args = (len(threads), l_start, steps)))
    for t in threads:
        print("starting thread...")
        t.start()
    for t in threads:
        t.join()

    stoptime = datetime.now()
    print(f"time elapsed with {no_threads}: ", stoptime - starttime)
    pass
