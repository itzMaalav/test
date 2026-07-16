def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print('choose an operation:')
print('1. add')
print('2. subtact')
print('3. multiply')
print('4. divide')

try:
    choice = input('enter choice 1/2/3/4: ')
    if choice == '1':
        print('result:', add(num1, num2))
    elif choice == '2':
        print('restult:', subtract(num1, num2))
    elif choice == '3':
        print('restult:', multiply(num2, num2))
    elif choice == '4':
        try:
            print('result:', divide(num1, num2))
        except ZeroDivisionError:
            print('cannot divide by zero!')
