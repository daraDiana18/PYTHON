a = int(input('First number: '))
b = input('Operation: ')
c = int(input('Second number: '))
if b == '+':
    S = a+c
    print(a, b, c,'=', S)
elif b == '-':
    S = a-c
    print(a, b, c,'=', S)
elif b == '/':
    if c != 0:
        S = a/c
        print(a, b, c,'=', S)
    else:
        print('Cannot be divided by 0')
elif b == '*':
    S = a*c
    print(a, b, c,'=', S)

  
