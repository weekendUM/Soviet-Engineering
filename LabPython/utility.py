def gcd(a : int, b : int):
    r = a%b
    while(r>0):
        a=b
        b=r
        r=a%b
    return b

def scm(a : int, b : int):
    return (a*b)//gcd(a,b)

def sgn(x : int):
    return (x>=0)



