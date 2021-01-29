v = [1,3,5,7,8,12]

def insert(el, left, right):
    if(left >= right):
        return left
    l1 = (left + right) // 2
    l2 = (left + right) // 2 + 1
    if(el > v[l1]):
        if(el < v[l2]):
            return l2
        else:
            return insert(el, l2 + 1, right)
    else:
        return insert(el, left, l1 - 1)

print(insert(6, 0, len(v) - 1))
