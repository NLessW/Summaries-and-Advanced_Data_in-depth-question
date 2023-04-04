a,b,c = map(int,input("세 정수를 입력하시오 : ").split())

if a>b and a>c and b>c:
    print(a,b,c)
elif a>b and a>c and b<c:
    print(a,c,b)
elif b>a and b>c and a>c:
    print(b,a,c)
elif b>a and b>c and a<c:
    print(b,c,a)
elif c>a and c>b and a>b:
    print(c,a,b)
else:
    print(c,b,a)
