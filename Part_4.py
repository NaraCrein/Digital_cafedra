from random import randint

# 1 task
print('TASK 1')
first = randint(0, 100)
second = randint(0, 100)
third = randint(0, 100)
print(f'({first} + {second} + {third}) / 3 = {(first+second+third)/3}')

# 2 task
print('\nTASK 2')
x = randint(100, 200)
y = randint(1, 100)
print(f'x = {x} and y = {y}\nResult: {x//y}, {x%y}')

# 3 task
print('\nTASK 3')
x = 14.7212
print(f'x = {x}')
print('1) {0:.2f}'.format(x))
print('2) {0:.0f}'.format(x))
print('3) {0:011}'.format(x))

# 4 task
print('\nTASK 4')
print('Enter x:')
y = input()
n = len(y)
x = int(y)
result = 0
i = 0
key = 1
if x < 0:
    key = -1
    x *= -1
    n -= 1
for i in range(0, n):
    result += (x % 10) * 10 ** (n-i-1)
    x //= 10
    i += 1
result *= key
print(f'Your result: {result}')

# 5 task
print('\nTASK 5')
print('Enter x:')
y = input()
n = len(y)
x = int(y)
result = 0
i = 0
key = 1
if abs(x) <= 0xffffffff:
    print(f'Your result: {result}')
else:
    if x < 0:
        key = -1
        x *= -1
        n -= 1
    for i in range(0, n):
        result += (x % 10) * 10 ** (n-i-1)
        x //= 10
        i += 1
    result *= key
    print(f'Your result: {result}')
