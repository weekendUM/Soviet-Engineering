a= [3,1,5,10]
b= [4,2,6,1]
c= [5,3,1,7]
op = 0

def n3():
    global op
    rez = False
    for i in a:
        for j in b:
            for k in c:
                op += 1
                if(i==j==k):
                    rez = True
    return rez



def n2():
    global op
    rez =  False
    for i in a:
        for j in b:
            op += 1
            if(i==j):
                for k in c:
                    op += 1
                    if(i==k):
                        rez = True
                        break
    return rez

def maxnm(m : int):
    global op
    rez = False
    n = len(a)
    ap = [0] * (m + 1)
    for i in a:
        op += 1
        ap[i] += 1
    for i in b:
        op += 1
        ap[i] += 1
    for i in c:
        op += 1
        ap[i] += 1
    for i in ap:
        op += 1
        if(i == 3):
            rez = True
    return rez

def merge():
    global op
    rez = False
    i  = 0
    j = 0
    while(i != len(a)-1 and j != len(b)-1):
        if(a[i] != b[j]):
            pass
    return rez


print(n3(), op)
op = 0
print(n2(), op)
op = 0
print(maxnm(10), op)
op = 0
print(merge(), op)