import math
x=float(input('x: '))
y=float(input('y: '))

a= 5*x*y
b=math.pow(x,3)-4
c= a/b

d=math.exp(math.pow(x,2))

e=math.sqrt((math.pow(math.cos(y),2))- math.pow(y,2))

f= c+d+e

print ('f=', f)
