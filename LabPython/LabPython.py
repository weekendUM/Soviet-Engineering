x = [1,3,4,6,8,10,12]

def rotate(k = 1):
    global x
    buffer = []
    for i in range(len(x)-k,len(x)):
        buffer.append(x[i])
    for i in range(len(x)-k):
        buffer.append(x[i])
    
    x = buffer

def binarySearch(el, left, right):
    if(left == right):
        if(el == x[left]):
            return True
        return False
    mid = (left + right) // 2
    if(el == x[mid]):
        return True
    elif(el < x[mid]):
        return binarySearch(el, left, mid - 1)
    elif(el > x[mid]):
        return binarySearch(el, mid + 1, right)

def findEl(el, breakpoint = 1):
    return binarySearch(el, 0, breakpoint - 1) or binarySearch(el, breakpoint, len(x)-1)

def findBreakpoint(left, right):
    if(right < left): return -1
    if(left == right): return left
    mid = (left + right) // 2
    if(mid < right and x[mid + 1] < x[mid]):
        return mid
    if(mid > left and x[mid] < x[mid - 1]):
        return mid - 1

    if(x[left] > x[mid]):
        return findBreakpoint(left, mid - 1)
    return findBreakpoint(mid + 1, right)



k = 3
print(x)
rotate(k)
print(x)
print(findEl(7, findBreakpoint(0, len(x) - 1) + 1))



