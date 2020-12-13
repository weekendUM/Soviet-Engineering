
#import test_class
import __future__
#from fractions import fraction
#from polynomial import polynomial
#from fractions import fraction
#import prime
#import medie_note
#import dictionary1
#import prime_factors
#import base_conversion as bc
import json
import csv

#x = int(input("Numar: "))
print("おはよう世界　Good morning World!")
#a = fraction(-1)
#test = polynomial(1,-6,9)
#print(test.calc_value(fraction(1)))
#for i in test.calc_roots():
  #  print(i,end=' ')

with open("air_quality.json") as file:
    data = json.load(file)

fields = []

for buffer in data["meta"]["view"]["columns"]:
    fields.append(buffer["name"])
#print(fields)
with open("air_quality.csv","w") as out:
    write = csv.writer(out)
    write.writerow(fields)
    write.writerows(data["data"])


#json.detect_encoding(data)


#print(a**7)

#print(bc.to_binary(12))


#print(prime.prim(138857))
