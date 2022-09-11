import math

def Roots(a, b, c):  
  
    d = b * b - 4 * a * c  
    
  
  
    if d > 0:  
        print("answer")  
        print((-b + math.sqrt(d)) / (2 * a))  
        print((-b - math.sqrt(d)) / (2 * a))  
  
    elif d == 0:  
        print("answer")  
        print(-b / (2 * a))  
  
  
    else:  
        print("no roots")

     
a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))

if a == 0:  
    print("its incorrect equation")
    
  
else:  
    Roots(a, b, c)  
  
       
  
  


