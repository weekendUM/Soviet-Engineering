x = [1,3,4,6,8,10,12]

def rotate(k = 1):
    global x
    buffer = []
    for i in range(len(x)-k,len(x)):
        buffer.append(x[i])
    for i in range(len(x)-k):
        buffer.append(x[i])
    
    x = buffer

print(x)
rotate(3)
print(x)

