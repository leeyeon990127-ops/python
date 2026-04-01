N = int(input())
#print(N)

def i():
    print(N, "+", int(10), "=", N+10 )
i()

def i():
    print(N, "-", int(10), "=", N-10)
i()    

#정수N에 +10/-10이 아니라 숫자 10을 넣어야 정수값이 변해도 결과가 달라지지 않는다.

#2----------------------
N = int(input())
#print(N)

def i_plus():
    print(f"{N} + 10 = {N + 10}")
i_plus()
def i_minus(): 
    print(f"{N} - 10 = {N - 10}")
i_minus()


#2-------------------------------------리턴 사용
def func_plus(param):
    return param + 10

def func_minus(param):
    return param - 10

inp = int(input())
#print(inp)
ret1 = func_plus(inp)      #ret는 return의 약자
ret2 = func_minus(inp)
print(f"{inp} + 10 = {ret1}")
print(f"{inp} - 10 = {ret2}")