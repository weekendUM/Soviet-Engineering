def factors(x):
    counter = 0 #cu asta numaram de cate ori apare un factor
    while (x % 2 == 0):
        counter += 1
        x = x / 2
    if(counter > 0):
        print("2 la puterea ", counter)
    d = 3
    counter = 0
    while (x > 1 and x >= d):
        #print("got here...")
        counter = 0
        while(x % d == 0):
            #print("got here...")
            #print(x)
            counter = counter + 1
            x = x / d
        if (counter):
            print(d, " la puterea ", counter)
        d = d + 2
        
