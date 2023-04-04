print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
cal = int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
a, b = map(int, input('연산을 원하는 숫자 두 개를 입력하세요: ').split())
 
if cal == 1 :
    print(a, '+', b, '=', a + b)
 
elif cal == 2 :
    print(a, '-', b, '=', a - b)
 
elif cal == 3 :
    print(a, '*',b, '=', a * b)
 
elif cal == 4 :
    print(a, '/', b, '=', a / b)
 
else :
    print('잘못 입력하였습니다.')
