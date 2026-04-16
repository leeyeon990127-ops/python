T = int(input())
#print(t)

for test_case in range(1, T+1):
    ch = input()   #변수선언
    if ch.islower():                      #islower 함수:
        print(f"{test_case} {ch} 는 소문자 입니다.")
    else:
        print(f"{test_case} {ch} 는 대문자 입니다.")


#2---------------------------------------
def ask(word):
    code = ord(str(word))
    if 65 <= code <= 90:
        return '대문자'
    elif 97 <= code <= 122:
        return '소문자'

TC = int(input())

for i in range(1, TC + 1):
    alpha = input()
    S = ask(alpha)
    print(f'#{i} {alpha} 는 {S} 입니다.')