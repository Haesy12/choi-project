#제목: 연산자와 ofrmat () Review
#이름: 최민혁
import datetime

# a=int(input("a는 숫자로 입력:"))
# a//=2 # a= a//2
# print("a:",a ,type(a))
# a%=3 #a=a % 3
# print("a:",a ,type(a))
now= datetime.datetime.now()
print(now.year,"년", now.month, "월",now.day,"일")
print("{}년{}월{}일".format(now.year, now.month, now.day))
print(f"{now.year}년 {now.month}월 {now.day}일")