#이름:최민혁

#변수에 키보드로 데이터 입력
n = input("정수 입력:")
n = int(n)

#양수 조건
if n > 0:
    print(n, "는 양수입니다.")
    print("네 맞습니다.")

#음수 조건
if n < 0:
    print(n, "는 음수입니다.")

#0 조건
if n == 0:
    print("0 입니다.")