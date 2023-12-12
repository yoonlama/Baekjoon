# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

import sys
input=sys.stdin.readline
n=[]

for i in range(9):
    a=int(input())
    n.append(a)

print(max(n))
print(n.index(max(n))+1)