import utility

class fraction:
    numerator = int()
    denominator = int()

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
        buffer = self
        for i in range(1,power):
            #print("pasul: ", i)
            buffer *= self
        if(power==0):
            return 1

        return buffer

    def __hash__(self):
        return str(f"{self.numerator}/{self.denominator}").__hash__()

            

    def __str__(self):
        if(self.numerator%self.denominator):
            return f"{self.numerator}/{self.denominator}"
        return f"{self.numerator//self.denominator}"
