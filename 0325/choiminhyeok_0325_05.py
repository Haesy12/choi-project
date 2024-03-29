#이름:최민혁

# 입력
ch = input("숫자를 입력하세요")
print(ch)

#문자열 ch에서 마지막 문자 출력
print(ch[-1])
print(type(ch))

#문자를 숫자로 변환: cast
number = int(ch[-1])

#짝수 홀수 구분
if number == 0 or number ==2 \
    or number == 4 or number == 6 \
    or number == 8:
        print("짝수입니다.")
else:
    print("홀수입니다.")

    