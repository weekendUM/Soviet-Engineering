a = [1, 3, 5, 11]
b = [3, 7, 11, 13]

def greedy():
    helper = [] #list of valid segments
    for i in range(len(a)):
        valid = True
        for el in helper:
            if(a[i] > el[0] and a[i] < el[1]):
                valid = False
                break
        if(valid):
            helper.append((a[i],b[i]))
    print(helper)

greedy()

#T(n)=nk where k is the number of valid segments up to a certain point
#for many disjunct segments k will be very close to n