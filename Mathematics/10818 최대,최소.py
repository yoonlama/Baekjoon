#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
print(min(b),max(b))