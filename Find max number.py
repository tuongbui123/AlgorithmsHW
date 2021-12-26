def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest

number1 = input('Enter first number: ')
a = int(number1)
number2 = input('Enter second number: ')
b = int(number2)
number3 = input('Enter third number: ')
c = int(number3)

print(f"The max number is : {maximum(a,b,c)}")
