# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
a=input()
if 90<=int(a)<=100:
    print("A")
elif 80<=int(a)<90:
    print("B")
elif 70<=int(a)<80:
    print("C")
elif 60<=int(a)<70:
    print("D")
else:
    print("F")