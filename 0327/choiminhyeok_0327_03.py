# 제목 : 1~n까지의 x 배수의 합 구하기
# 이름 : 최민혁

#정수 n 입력
n = int(input("입력(까지) n:"))

#x 배수 입력
x = int(input("입력 (배수)x:"))

sum = 0

#for와 if문 들여쓰기 철저하게 할 것
for i in range(0, n+1, 1):
    if i % x == 0:
        sum = sum + i 
        print("i=%d" % i, "sum=%d" % sum)

