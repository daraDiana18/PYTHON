import math
print("Choose your figure:")
print("Circle")
print("Rectangle ")
print("Triangle ")
figure = input("")
if figure == "Circle":
    r = float(input("r: "))
    area = math.pi * math.pow(r, 2)
    print("The area is :" + format(area))
    
if figure == "Rectangle":
    a = float(input("a: "))
    b = float(input("b: "))
    area = a * b
    print("The area is :" + format(area))
    
if figure == "Triangle":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area is :" + format(area))
