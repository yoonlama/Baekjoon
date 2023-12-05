# 혜아가 N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?
byte=int(input())
for i in range(byte // 4):
    print('long',end=' ')
print('int')

# 다른 방법
import sys
byte=int(sys.stdin.readline())

for i in range(byte // 4):
    print('long',end=' ')
print('int')