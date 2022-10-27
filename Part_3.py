# 1 task
print('TASK 1')
name = 'Natalya'
surname = 'Yakovleva'
print(f'Hello {name} {surname}! You just delved into Python. Great start!')

# 2 task
print('\nTASK 2')
marker = 'E'
thickness = 5
for i in range(thickness):
    print((marker*i).rjust(thickness-1) + marker + (marker*i).ljust(thickness-1))
# Top Pillars
for i in range(thickness+1):
    print((marker*thickness).center(thickness*2) + (marker*thickness).center(thickness*6))
# Middle Belt
for i in range((thickness+1)//2):
    print((marker*thickness*5).center(thickness*6))
# Bottom Pillars
for i in range(thickness+1):
    print((marker*thickness).center(thickness*2) + (marker*thickness).center(thickness*6))
# Bottom Cone
for i in range(thickness):
    print(((marker*(thickness-i-1)).rjust(thickness) + marker + (marker*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# 3 task
print('\nTASK 3')
text = 'text for title'
print(text.title())

# 4 task
print('\nTASK 4')
amount = 100500.18777
print('{0:,.2f}'.format(amount))

# 5 task
print('\nTASK 5')
print('Enter height of carpet: ')
height = int(input())
width = 3*height
print(f'Your height: {height}\nYour width: {width}')

# 6 task
print('\nTASK 6')
print('Enter value: ')
value = int(input())
result = 1
while value != 0:
    result *= value % 10
    value //= 10
print(f'Result: {result}')
