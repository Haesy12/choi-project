#이름:최민혁

#입력
number = input("정수 입력:")
number = int(number)

# 짝수 조건: f string
if number % 2 == 0:
    print(f"{number}은 짝수")

# 홀수 조건: format() 함수
if number % 2 ==1:
    print("{}은 홀수".format(number))
