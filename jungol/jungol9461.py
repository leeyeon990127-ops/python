a, b= map(int,input().split())
#print(a, b)

def get_number():
    print(f"{a * 2} {b // 2}")
    
get_number()    

############### #########################################################
a, b= map(int,input().split())
#print(a, b)

def get_number(pa, pb):
    global a, b  # 지금부터 이 함수 안에서 쓰는 a, b는 바깥의 메인 저장소다
    a = pa * 2 # pa비구니에 담긴값에 2를 곱한다.
               # 그 결과값을 a(메인 저장소)에 집어넣습니다. (기존 값은 덮어씌워짐)
    b = pb // 2  # pb(바구니)에 담긴 값을 2로 나눕니다.
                 # 그 결과값을 b(메인 저장소)에 집어넣습니다
   
get_number(a, b)
print(f"{a} {b}")

#2 ############################################################################
a, b= map(int,input().split())
#print(a, b)
def calc():
    global a, b
    if a > b:
        a //= 2
        b *= 2
    else:
        b //= 2
        a *= 2

calc()
print(a, b)

