import math

def prim (n):
    if (n == 2):
        return True
    if (n < 2 or n % 2 == 0):
        return False    
    for i in range(3, int(math.sqrt(n)), 2):
        print(i)
        if (n % i == 0):
            return False
    return True