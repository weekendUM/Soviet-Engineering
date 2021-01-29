a = [5,3,7]
b = [3,7,9]

class number:
    def __init__(self, arr = [0]):
        self.arr = arr

    def __gt__(self, other):
        arr = self.arr
        guest = other.arr
        for i in range(len(arr) - 1):
            if(arr[i] > guest[i]):
                return 1
            elif(arr[i] < guest[i]):
                return -1

        if (arr[-1] > guest[-1]):
            return 1
        return -1

    def __add__(self, other):
        res = []
        carry = 0
        arr = self.arr
        guest = other.arr
        for i in range(len(arr) - 1, -1, -1):
            new = (arr[i] + guest[i] + carry) % 10
            res.append(new)
            carry = (arr[i] + guest[i] + carry) // 10
        return number(reversed(res))

    def __str__(self):
        res = str()
        for el in self.arr:
            res += str(el)
        return res

    def __sub__(self, other):
        for i in range(len(other.arr)):
            other.arr[i] = -other.arr[i]
        return self + other
        

n1 = number(a)
n2 = number(b)
print(n1 > n2)
print(n1 + n2)
print(n1 - n2)