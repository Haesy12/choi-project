#제목: 다양한 텍스처 처리함수 Review
#이름:최민혁

#strip ()함수
string1 = "  선 문 대학  교     "
string2 = "  a b cd  e     "
s = string2.lstrip()
sp = string1.split()
f = string1.find("대학")
i = string1 in "학"
print(s, type(s))
print(sp, type(sp))
print(f,type(f))
print(i,type(i))
    