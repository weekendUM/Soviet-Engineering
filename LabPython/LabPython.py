#import test_class
import __future__
from fractions import fraction
from polynomial import polynomial
#import prime
#import medie_note
#import dictionary1
#import prime_factors

#x = int(input("Numar: "))
print("Hello 世界")
test = polynomial(1,-6,9)
#print(test.calc_value(fraction(1)))
for i in test.calc_roots():
    print(i,' ',end='')
print()


#print(prime.prim(138857))