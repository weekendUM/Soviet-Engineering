from binary import binary

def to_binary(number : int, k = 16):
    bin=[0]*k
    #print(bin)
    if(number<0):
        bin[-1]=1


    i = 0
    while(number):
        bin[i]=number%2
        i+=1
        number //=2
    #print(bin)
    #tpl = tuple()
    bin.reverse()
    number=binary(bin)
    #print(number)
    return number
