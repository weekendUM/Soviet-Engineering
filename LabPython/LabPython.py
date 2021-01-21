import os

word1 = 'caiet'
word2 = 'cort'

dis = []

ex = -1

for i in range(len(word1)):
    buffer = []
    for j in range(len(word2)):
        buffer.append(0)
    dis.append(buffer)

if(word1[0]==word2[0]):
    dis[0][0]=0
else:
    dis[0][0] = 1

def calc_dist(i, j):
    global ex
    ex += 1
    if(i==j and i==0):
        return dis[0][0]
    if(j==0):
        dis[i][j] = i
        return dis[i][j]
    if(i==0):
        dis[i][j] = j
        return dis[i][j]
    if(word1[i]==word2[j]):
        if(dis[i][j]!=0):
            return dis[i][j]
        else:
            dis[i][j] = calc_dist(i-1,j-1)
            return dis[i][j]
    if(word1[i]!=word2[j]):
        if(dis[i][j]!=0):
            return dis[i][j]
        else:
            dis[i][j] = min(calc_dist(i-1,j-1),calc_dist(i,j-1),calc_dist(i-1,j)) + 1
            return dis[i][j]



try:
    print("Distanta de editare cu memoizare:", calc_dist(len(word1) - 1,len(word2) - 1))
    print("Apeluri de functii recursive efectuate cu memoizare:", ex)
    ex = -1
    for l in dis:
        print(l)
except:
    print('failed')

try:
    cls = int(input("Doriti sa executam programul si fara memoizare?(raspundeti cu 1 pt adevarat)\nRaspuns: "))
except:
    os._exit(0)

if(cls == 1):
    print('Incepem fara memoizare')
    def calc_disti(i, j):
        global ex
        ex += 1
        if(i==j and i==0):
            if(word1[0]==word2[0]):
                return 0
            else:
                return 1
        if(j==0):
            return i
        if(i==0):
            return j
        if(word1[i]==word2[j]):
            return calc_disti(i-1,j-1)
        if(word1[i]!=word2[j]):
            return min(calc_disti(i-1,j-1),calc_disti(i,j-1),calc_disti(i-1,j)) + 1

    try:
        print("Distanta de editare fara memoizare:", calc_disti(len(word1) - 1,len(word2) - 1))
        print("Apeluri de functii recursive efectuate fara memoizare:", ex)
    except:
        print('failed')
else:
    pass