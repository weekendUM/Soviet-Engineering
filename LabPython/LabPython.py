from math import sqrt

A = [
    [2, 3, 5],
    [1, 1, 4],
    [2, 2, 6],
    [3, 3, 1]
    ]

e_norm = []

cursor = 0

def mergesort(arr):
    global cursor
    if(len(arr) == 2):
        if(arr[0] > arr[1]):
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr
        return arr
    else:
        arr[:len(arr)//2] = mergesort(arr[:len(arr)//2])
        cursor = len(arr)//2
        arr[len(arr)//2:] = mergesort(arr[len(arr)//2:])
        buffer = []
        i = 0
        j = 0
        #while()
        return arr
    pass

for line in A:
    buffer = 0
    for i in line:
        buffer += i**2
    e_norm.append(sqrt(buffer))

print(e_norm)