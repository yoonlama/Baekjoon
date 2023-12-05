# 45분 일찍 알람 설정하기
h,m=map(int,input().split())

if h!=0 and m<45:
    print(h-1,m+15)
elif h==0 and m< 45:
    h=23
    print(h,m+15)
elif m==45:
    m=0
    print(h,m)
else:
    print(h,m-45)