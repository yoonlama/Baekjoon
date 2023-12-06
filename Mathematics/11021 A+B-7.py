# A+B
import sys
c=int(sys.stdin.readline())
lst=[]
j=0


for i in range(c):
    a,b=map(int,sys.stdin.readline().split())
    lst.append(a+b)

for i in range(c):
    j+=1
    print(f'Case #{j}:',lst[(i)])