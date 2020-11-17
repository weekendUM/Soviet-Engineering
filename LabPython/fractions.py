import utility

class fraction:
    numerator = int()
    denominator = int()
    powers = {}

    def simplify(self):
        divisor = utility.gcd(self.numerator, self.denominator)
        
        self.numerator //=divisor
        self.denominator //=divisor

    def __init__(self, *args):
        #print(args)
        if(len(args)==2):
            a=args[0]
            b=args[1]
            if(utility.sgn(a)!=utility.sgn(b)):
                if(utility.sgn(b)==0):
                    #print("negative denominator")
                    a = -a
                    b = -b
            self.numerator=a
            self.denominator=b
            self.simplify()
        else:
            self.__init__(args[0], 1)


    def __add__(self, other):
        #print(type(other))
        if(self.denominator!=other.denominator):
            com_d=utility.scm(self.denominator,other.denominator)
            x = self.numerator* (com_d//self.denominator) + other.numerator*(com_d//other.denominator)
        else:
            x = self.numerator+other.numerator
            com_d=self.denominator
        return fraction(x,com_d)

    def __truediv__(self, other):
        buffer = fraction(other.denominator, other.numerator)
        return self * buffer

    def __sub__(self, other):
        buffer = fraction(-other.numerator, other.denominator)
        return buffer + self

    def __mul__(self, other):
        x = self.numerator * other.numerator
        #print(x)
        y = self.denominator * other.denominator
        #print(y)
        return fraction(x,y)

    def __eq__(self, other):
        if(self.numerator!=other.numerator):
            return False
        if(self.denominator!=other.denominator):
            return False
        return True

    def __pow__(self, power : int):
        if(power==0):
            #print("putere 0")
            return 1
        if(power==1):
            #print('fractia este ',self*self)
            #print("putere 1: ",self)
            return self
        elif(power%2==0):
            #print("putere para")
            if((power//2 in self.powers)==0):
                if(power//2 in [0,1]):
                    return self**(power//2)*self**(power//2)
                self.powers[power//2] = self**(power//2)
                #print(power//2)
                #print(f"puterea pt {power//2} este",self**(power//2))
                return self.powers[power//2]*self.powers[power//2]
            #print(f"puterea pt {power//2} este",self**(power//2))
            return self.powers[power//2]*self.powers[power//2]
        else:
            #print(f"in else cu {power}")
            #print("putere impara")
            if((power//2 in self.powers)==0):
                self.powers[power//2] = self**(power//2)
                return self.powers[power//2]*self.powers[power//2]*self
            
            return self.powers[power//2]*self.powers[power//2]*self
        

        return fraction(1)

    def __hash__(self):
        return str(f"{self.numerator}/{self.denominator}").__hash__()

            

    def __str__(self):
        if(self.numerator%self.denominator):
            return f"{self.numerator}/{self.denominator}"
        return f"{self.numerator//self.denominator}"
