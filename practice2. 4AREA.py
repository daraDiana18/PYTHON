import math

AB = float(input ('AB:'))
AC = float(input ('AC:'))


BC = math.sqrt (math.pow(AB,2) + math.pow(AC,2))

S = (AB * AC) / 2
P = AB + AC + BC

print ('area', S)
print ('perimeter', P)
