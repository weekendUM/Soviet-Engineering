def divisors(number : int,own=False):
    div=[]
    if(number<0):
        number=-number
    if(own==0):
        div.append(1)
    for i in range(2, number//2+1):
        if(number%i==0):
            div.append(i)
    if(own==0 and number!=1 and number!=0):
        div.append(number)

    return div