class binary:
    def __init__(self, args = []):
        #print(args)
        self.no_bits=len(args)
        self.bits=args

    #getters
    def get_no_bits(self): return self.no_bits
    def get_bits(self): return self.bits

    def __add__(self,other):
        carried_bit = 0
        new_bits=[]
        if(other.get_no_bits()>self.no_bits):
            for i in range(other.no_bits()):
                for j in range(self.no_bits):
                    buffer = self[j] + other[i] + carried_bit
                    if(buffer==0):
                        new_bits.append(0)
                    elif(buffer>=1):
                        new_bits.append(1)
            
        pass
        

    def __getitem__(self, index:int):
        return self.bits[index]

    #functions
    def __str__(self):
        out = str()
        for i in self.bits:
            out+=str(i)
        return out

    def dec(self):
        bits = self.bits
        carry = 1
        for i in range(len(bits) - 1, -1, -1):
            if(carry == 1):
                if(bits[i] == 1):
                    bits[i] = 0
                    break
                else:
                    bits[i] = 1
        return binary(bits)
