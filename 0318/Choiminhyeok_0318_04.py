#제목:1-100까지의 숫자 중 짝수의 합
#     복합 대입연산자, for반복문, if 조건문
#이름:최민혁

n=int(input("n을 입력하세요:"))
s=0

for i in range(n+1):
    if(i % 2 == 0):
        s+=i #s=s+i
        # print("i:", i,"s:",s )
        print("i: {}s:{}".format(i,s))


