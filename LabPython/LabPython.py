class date:
    def __init__(self, year = 2000, month = 1, day = 1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self): return f"({self.year}-{self.month}-{self.day})"        

    def __repr__(self): return str(self)

    def __gt__(self, other):
        if(self.year > other.year):
            return True
        elif(self.year < other.year):
            return False
        else:
            if(self.month > other.month):
                return True
            elif(self.month < other.month):
                return False
            else:
                if(self.day > other.day):
                    return True
                else:
                    return False

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        return (not self == other) and (not self > other)

def mergesort(arr):
    if(len(arr) == 1):
        return arr
    elif(len(arr) == 2):
        if(arr[0] > arr[1]):
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
            return arr
        return arr
    else:
        arr[:len(arr)//2] = mergesort(arr[:len(arr)//2])
        arr[len(arr)//2:] = mergesort(arr[len(arr)//2:])
        buffer = []
        i = 0
        j = len(arr)//2
        while(i < len(arr)//2 and j < len(arr)):
            if(arr[i]<arr[j]):
                buffer.append(arr[i])
                i += 1
            else:
                buffer.append(arr[j])
                j += 1
        if(i<len(arr)//2):
            buffer.extend(arr[i:len(arr)//2])
        elif(j<len(arr)):
            buffer.extend(arr[j:])
        return buffer

lst = [date(), date(1990), date(1990,7,23), date(2000,1,3)]
print(lst)
lst = mergesort(lst)
print(lst)
