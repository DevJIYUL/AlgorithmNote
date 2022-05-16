#TOP-DOWN DP(fibonacci)
#메모이제이션 기법 사용
#=>이전에 한 계산 결과를 일시적으로 저장해놓은 개념
d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99))

#BOTTOM-UP DP(fibonacci)
#DP테이블 사용
#=>결과 저장용 리스트
d =[0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])