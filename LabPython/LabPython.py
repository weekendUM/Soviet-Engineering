def poz(x : list, v):
    if(v < x[0]):
        return 0
    elif(v > x[-1]):
        return len(x)
    else:
        for i in range(len(x) - 1):
            if(v < x[i+1] and v > x[i]):
                return i+1

def alg(x = [3,6,2,7,5]):
    for i in range(1,len(x)):
        a = x[i]
        j = poz(x[:i], x[i])
        for k in range(i-1, j-1, -1):
            x[k+1] = x[k]
        x[j]=a
    return x

print(alg())