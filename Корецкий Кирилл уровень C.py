import  random
#1
lst = [random.randint(-1000, 1000) for i in range(random.randint(5, 100))]
print(lst)
sm = 0
for i in range(len(lst)):
    if lst[i] > 0:
        sm = sm + lst[i]
print(sm)
#2
lst.clear()
for i in range(random.randint(0,100)):
    lst.append(i)
print(lst)
try:
    num = int(input())
    if lst[0] < num < lst[-1]:
        print('да')
    else:
        print('нет')
except(ValueError):
    print('ЧИСЛО!!!')
#3
lst.clear()
import random
try:
    n = int(input())
except(ValueError):
    print('ЧИСЛО!!!')
lst = [random.randint(1,15)for i in range(n)]
max = 0
min = lst[0]
print(lst)
for i in range(n):
    if max < lst[i]:
        max = lst[i]
print(max)
for i in range(n):
    if min > lst[i]:
        min = lst[i]
print(min)