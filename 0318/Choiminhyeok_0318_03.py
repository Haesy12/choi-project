#제목:원의 둘레와 넓이 구하기
#이름:최민혁

pi=3.1415922654
r=int(input("반지름 r을 입력하세요"))

print("원주율=",pi)
print("반지름=",r,type(r))
print("원의 둘레=",2*r*pi)
print("원의 넓이 = ",r**2*pi)