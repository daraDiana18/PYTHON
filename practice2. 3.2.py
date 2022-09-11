import math
x=float(input('x: '))
y=float(input('y: '))
z=float(input('z: '))


a=math.pow(math.fabs(math.cos(y)/ math.sin(y)),1/3)
b= math.sqrt(math.pow((x+1),3)/((4*y)- (2*z)))

c= a+b

print ('answer:', c)
