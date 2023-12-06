# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
total=int(input())
count=int(input())
sum=0

for i in range(count):
    a,b=map(int,input().split())
    r=a*b
    sum += r

if sum==total:
    print("Yes")
else:
    print("No")
