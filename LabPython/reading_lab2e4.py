l = [1, 4, 6, 0, 0, 3, 4, 2, 1, 9]
f = [0]*10
i = 0
for i in range(len(l)):
    f[l[i]] += 1
    i += 1
print ("f=", f)
