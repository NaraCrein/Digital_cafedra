# 1 task
import random

print('TASK 1')
x = int(input('Enter your number: '))
if x % 5 == 0 and x % 3 == 0:
    print('Fizz Buzz')
elif x % 5 == 0:
    print('Fizz')
elif x % 3 == 0:
    print('Buzz')
else:
    print(f'{x}')

# 2 task
print('\nTASK 2')
x = int(input('Введите число x: '))
if x % 2 != 0:
    print('Плохо')
elif 2 < x < 5:
    print('Неплохо')
elif 6 < x < 20:
    print('Так себе')
elif x > 20:
    print('Отлично')

# 3 task
print('\nTASK 3')
N = random.randint(1, 10)
print(f'N = {N}')
for i in range(0, N):
    print(i+1)

# 4 task
print('\nTASK 4')
text = "How are you? Eh, ok. Low or Lower? Ohhh."
n = len(text)
print(n)
result = ''
for i in range(0, n):
    if text[i].istitle():
        result += text[i]
print(result)

# 5 task
print('\nTASK 5')
text = input('Enter string: ')
string_list = text.split()
n = len(string_list)
count = 0
for i in range(0, n):
    if string_list[i].isalpha():
        count += 1
        if count == 3:
            print('True')
            break
    else:
        count = 0
    if i == n-1 and count < 3:
        print('False')

# 6 task
print('\nTASK 6')
text = ["bright aright", "ok"]
n = len(text)
result = ''
for i in range(0, n-1):
    result += text[i] + ','
result += text[n-1]
print(result.replace('right', 'left'))
