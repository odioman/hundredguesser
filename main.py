import random

a = random.randint(1, 101)
usernum = int(input('Enter a number 1 to 100 to guess if you are right'))

if usernum == a:
    print('you got the right number!')

elif a > usernum:
    dif1 = a - usernum
    print('you are off by', dif1)

else:
    dif2 = usernum - a
    print('you are off by', dif2)