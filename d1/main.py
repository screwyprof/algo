# Program which is solving easy arithmetic operations

from arithmetic import arithmetic

a = int(input('Type first number: '))
b = int(input('Type second number: '))
c = str(input('Type necessary operation: '))

print('The answer is: ' + str(arithmetic(a, b, c)))
