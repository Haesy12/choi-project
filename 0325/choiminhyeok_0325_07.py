#이름:최민혁

score = int(input("성적을 입력하세요:"))

if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'

print(f"학점은 {grade} 입니다.")
    
    