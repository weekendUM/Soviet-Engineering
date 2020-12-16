import threads
from datetime import datetime

steps = 100000

def iterate(thread : int,start : int, stop : int):
    j = 0
    k = 1
    for i in range(start,stop):
        j += 1
        j /= steps
        j+=25
        for i in range(100):
            j += 2
        j = 0

threads.run(64, iterate, steps)
print("trying on a single thread")
starttime = datetime.now()
iterate(0, 0, steps)
print("time elapsed on a single thread: ", datetime.now() - starttime)