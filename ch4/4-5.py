import random

x = random.randint(0,9)
y = random.randint(0,9)
z = random.randint(0,9)

a,b,c = map(int,input("세 복권번호를 입력하시오 : ").split())


if a == x and b==y and c==z:
    print("상금 1억원")
elif a == x and b == y and c!=z:
    print("상금 1천만원")
elif a == x and b != y and c == z:
    print("상금 1천만원")
elif a != x and b==y and c==z:
    print("상금 1천만원")
elif a == x and b!=y and c!=z:
    print("상금 1만원")
elif a!=x and b==y and c!=z:
    print("상금 1만원")
elif a!=x and b!=y and c==z:
    print("상금 1만원")
else:
    print("디음 기회에...")
