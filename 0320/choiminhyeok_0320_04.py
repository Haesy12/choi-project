univ_1="선문대학교가 최고에요"
univ_2="서울 s대는 두번쨰에요"

a=univ_1.find("최고")
b=univ_2.find("최고")

c="최고" in univ_1
print(a); print(b); print(c)


d=univ_1.replace(' ','*')
print(d)

text1="동해물과\
백두산이\
마르고 닳도록\
하느님이\
보우하사\
우리나라 만세"

text2="""동해물과
백두산이
마르고 닳도록
하느님이
보우하사
우리나라 만세"""
print(text1)
lines1=text2.split("\n")
print(type(lines1))
print(lines1[0])
print(lines1[1])
print(lines1[2])
print(text2)
