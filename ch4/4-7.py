import random

x = random.randint(1,100)
y = random.randint(1,100)

a = int(input(str(x)+" + "+str(y)+" = " ))

if a==(x+y):
    print("잘했어요!")
else:
    print("정답은 ",x+y," 입니다")
