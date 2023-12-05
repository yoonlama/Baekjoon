#6 A+B
import sys
c=int(sys.stdin.readline())
lst=[]

for i in range(c):
    a,b=map(int,sys.stdin.readline().split())
    lst.append(a+b)

for i in range(c):
    print(lst[(i)])