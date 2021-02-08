def cautareBinara(el, l, r):
    if(r<=l):
        return l
    mid = (l+r) // 2
    if(x[mid] == el):
        return mid
    elif(el<x[mid]):
        return cautareBinara(el, l, mid - 1)
    else:
        return cautareBinara(el, mid + 1, r)
