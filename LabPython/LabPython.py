x = [4,7,2,3,9,10,13,1]


def alg(i,j):
    if(i==j):
        return x[i]
    else:
        m = (i+j)%2
        a = alg(i,m)
        b = alg(m+1,j)
        return a * b

try:
    print(alg(0,len(x)-1))
except Exception as e:
    print(e)