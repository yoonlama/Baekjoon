# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
t=int(input())
lst = []
for i in range(t):
    a,b=map(int,input().split())
    lst.append(a+b) #lst에 a+b를 추가 -> t만큼 반복

for i in range(t): #t만큼 lst의 i번째 값 출력
    print(lst[i])