#3 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
a=input()
if (int(a)%4==0 and int(a)%100!=0) or (int(a) % 400==0):
    print('1')
else:
    print('0')