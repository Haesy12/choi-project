# 제목 : 1~10까지 합을 구하는 프로그램
# 이름 : 최민혁
print("1부터 n까지의 합을 구하느 프로그램")
n = int(input("n을 입력하세요:"))
hap = 0 
for i in range(0, n+1, 2):
    hap = hap + i
    print("i:{} hap:{}".format(i,hap))

