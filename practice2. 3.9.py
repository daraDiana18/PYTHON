import math
x=float (input ('x:'))

a= math.pow(math.log1p(x-3),4) + math.pow(2,x)* math.pow(math.sin(3*x),2)
b= 4*x- 5.2
c=a/b

print('answer:', c)
