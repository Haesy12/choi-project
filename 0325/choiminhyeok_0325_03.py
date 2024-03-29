#이름:최민혁

#날짜/시간과 관련된 기능을 가져옴
import datetime

# 현재 날짜/시간을 구함
now = datetime.datetime.now()
print(now, type(now))
a = now.month
a = 1
# 오전 구분
if now.hour < 12:
    print(f"현재 시각은 {now.hour} 오전")
    #print("현재 시각은 {}".format(now.hour))

# 오전 오후
if now.hour >= 12:
     print(f"현재 시각은 {now.hour} 오후")

# 계정 구분: 봄
if 3 <= a <= 5:
    print(f"이번 달은 {a}월 봄")

# 계정 구분: 여름
if 6 <= a <= 8:
    print(f"이번 달은 {a}월 여름")

# 계정 구분: 가을
if 9 <= a <= 11:
    print(f"이번 달은 {a}월 가을")

# 계정 구분: 겨울
if 12 >= a <= 2:
    print(f"이번 달은 {a}월 겨울")
