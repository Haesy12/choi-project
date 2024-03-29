#이름:최민혁

# 입력
ch = input("숫자를 입력하세요:")
print(ch)
print(ch[-1])
print(type(ch))

# 문자열 ch에서 마지막 문자 추력
last_ch = ch[-1]
print("last ch=%c" % last_ch)

#in 연산자를 이용한 짝수와 홀수 구분
if last_ch in "02468":
        print("짝수입니다.")
else:
    print("홀수입니다.")
    
    