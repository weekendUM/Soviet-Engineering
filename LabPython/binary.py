class binary:
    def __init__(self, args = []):
        print(args)
        self.no_bits=len(args)
        self.bits=args

    #getters
    def get_no_bits(): return self.no_bits
    def get_bits(): return self.bits

    #functions
    def __str__(self):
        out = str()
        for i in self.bits:
            out+=str(i)
        return out
