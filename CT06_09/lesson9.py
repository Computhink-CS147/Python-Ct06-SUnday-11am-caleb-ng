# print("Hello from lesson 9")
# import random
# num1 = random.randint(1,6)
# num2 = random.randint(1,6)
# num3 = random.randint(1,6)
# print (num1,num2,num3)

# all_even_odd = (num1%2==0) and (num2%2==0) and (num3%2==0)
# print("all numbers are even/odd:", all_even_odd)

import random
numapples = random.randint(1, 10)
numoranges = random.randint(1,10)
if numapples>5:
    costapples = numapples * 0.60
else:
    costapples = numapples * 0.90
    if numoranges>5:
        costoranges= numoranges * 0.90
    else:
        costoranges = numoranges *0.90 * 90
totalcost = costapples + costoranges
print (totalcost)
print("end")
s=input("how many apples to buy")
if count>5:
    cost = count *10
else: print('cost is',) ''