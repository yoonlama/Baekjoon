# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

a,b,c=map(int,input().split())

if a==b==c:
    print(10000+(a*1000))
elif a==b or a==c or b==c:
    if a==b or a==c:
        print(1000+(a*100))
    else:
        print(1000+(c*100))
else:
    if a>b>c or a>c>b:
        print(a*100)
    elif b>a>c or b>c>a:
        print(b*100)
    else:
        print(max(a,b,c)*100)