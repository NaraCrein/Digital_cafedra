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
