#제목:텍스트 처리 다양한 함수
#이름:최민혁
text1="simple is better than complex."
text2= text1.replace('', '_')
text3= text1.replace('','_',2)
print("text1:", text1)
print("text2:", text2)
print("text3:", text3)

#문자열을 0으로 채우기 : zfill()
num=92
num_str= str(num)
zfiled=num_str.zfill(7)
print(zfiled)
#문자열을 왼쪽/오른쪽/가운데 정렳기
text4= "abc"
r_test = text4.rjust(6,'*') # 오른쪽정렬
l_test = text4.ljust(6,'*')
c_test = text4.center(6,'*')

print(r_test, l_test, c_test)

#특정 문자열 포함 행만 추출: split()
text5= """동해물과 백두산이 마르고
하느님이 보우하사 우리 나라만세"""
lines1=text5.split("\n")
print(lines1,":", type(lines1))
