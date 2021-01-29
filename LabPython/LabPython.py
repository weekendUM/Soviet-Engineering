A = [
    [3,6,10],
    [5,9,12],
    [11,14,16]
    ]

def searchEl(el):
    i = 0
    j = len(A[0]) - 1
    while(i != len(A) and j != -1):
        if(A[i][j] == el):
            return True
        elif(A[i][j] > el):
            j -= 1
            continue
        elif(A[i][j] < el):
            i += 1
            continue
        else: break
    return False

print(searchEl(3))
