#새로운 평균을 구하는 프로그램을 작성하시오.

import sys
input=sys.stdin.readline

c=int(input())

b=list(map(int,input().split()))

m=max(b)

ave=sum(b)*100/(c*m)

print(ave)