import math
x=float(input('x: '))
y=float(input('y: '))
z=float(input('z: '))

a=(4* math.fabs(x))-(x*y*math.pow(z,2))
b=(x+ math.exp(y*x))- (2*y*z)
c=a/b

print('answer:', c)
