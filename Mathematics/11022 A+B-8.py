#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys
c=int(sys.stdin.readline())
lst=[]
lsta=[]
lstb=[]
j=0


for i in range(c):
    a,b=map(int,sys.stdin.readline().split())
    lst.append(a+b)
    lsta.append(a)
    lstb.append(b)

for i in range(c):
    j+=1
    print(f'Case #{j}:',lsta[i],'+',lstb[i],'=',lst[i])