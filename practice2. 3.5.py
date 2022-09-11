import math
x=float(input('x: '))
y=float(input('y: '))
z=float(input('z: '))

a= math.pow(4, x*y)
b= math.pow(x, y*z)
c=math.pow(x*y, z)

d=a-b+c

print('answer:', d)
