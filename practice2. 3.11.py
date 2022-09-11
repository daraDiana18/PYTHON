import math
x=float (input ('x:'))
y=float (input ('y:'))

a=math.asin(math.pow(x,3))-6
b= 8*(math.cos(4*y)- math.sin(4*x))
c=a/b

print('answer:',c)
