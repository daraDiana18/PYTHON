import math
x=float(input('x: '))
y=float(input('y: '))
z=float(input('z: '))

a=math.fabs(math.pow(math.log1p(x),2))+ math.exp(2*x)
b=x+3.4
c= math.pow(math.cos(3/x*y*z)/ math.sin(3/x*y*z),3)

d= a/b-c

print('answer:', d)

