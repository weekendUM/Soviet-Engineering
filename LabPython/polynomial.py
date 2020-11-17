from fractions import fraction
import divisors

class polynomial:
    terms = []
    def __init__(self, *args):
        self.constants = args
    
    def calc_value(self, x):
        if(type(x)==fraction):
            return self._calc_fraction(x)
        pass


    def _calc_fraction(self, x : fraction):
        sum = fraction(0,1)
        terms=[]
        #print('x= ',x)
        for i in range(len(self.constants)-1,-1,-1):
            #print(self.constants[i])
            self.terms.append(fraction(self.constants[i])*(x**(len(self.constants)-(i+1))))
            #print(fraction(self.constants[i])*(x**(len(self.constants)-(i+1))))
            sum+=self.terms[-1]
            #print(sum)
        #print(sum)
        #print()
        return sum

    def calc_roots(self):
        sols=set()
        if(self.calc_value(fraction(0))==0):
            sols.add(fraction(0))
            pass
        if(self.constants[-1]==0):
            c0_div=set()
            c0_div.add(1)
            div=[]
            for c in self.constants[1:len(self.constants)]:
                div=divisors.divisors(c)
                for d in div:
                    c0_div.add(d)
        else:
            c0_div=divisors.divisors(self.constants[-1])
        #print(c0_div)
        cn_div=divisors.divisors(self.constants[0])
        #print(cn_div)
        if(len(c0_div)<len(cn_div)):
            for i in c0_div:
                for j in cn_div:
                    if(self.calc_value(fraction(i,j))==0):
                        sols.add(fraction(i,j))
                    if(self.calc_value(fraction(i,-j))==0):
                        sols.add(fraction(i,-j))
        else:
            for i in cn_div:
                for j in c0_div:
                    if(self.calc_value(fraction(j,i))==0):
                        sols.add(fraction(j,i))
                    if(self.calc_value(fraction(-j,i))==0):
                        sols.add(fraction(-j,i))

        return sols
