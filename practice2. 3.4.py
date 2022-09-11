import math
x=float(input('x: '))
y=float(input('y: '))

a= math.sqrt(math.fabs(y))
b=math.pow(math.atan(math.log1p(x)), 3)
c=math.pow(x,y)-y+1

d=b/c
e=a+d

print('answer:',e)
