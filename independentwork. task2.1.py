a = float(input('First number: '))
b = input('Operation: ')
c = float(input('Second number: '))
if b == '+':
    S = a+c
    print(a, b, c,'=', S)
elif b == '-':
    S = a-c
    print(a, b, c,'=', S)
elif b == '*':
    S = a*c
    print(a, b, c,'=', S)
elif b == '/':
    S = a/c
    print(a, b, c,'=', S)
