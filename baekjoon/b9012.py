T = int(input())  #테스트 케이스를 입력받기
#print()

for i in range(T):
    ps = input()   #문자열로 괄호 입력받기

count = 0  # 열린괄호의 개수판
res = True

for x in ps():
    if x == "(":
        count += 1 # 열린 괄호면 숫자를 늘린다
    else:
        count -= 1 # 닫힌 괄호면 숫자를 줄인다

    if x < 0:      # 숫자가 음수가 되면 중단한다
        break

    if res and count == 0: # 숫자가 딱 0 이어야 하고 중간에 오류가 없어야 한다다
        print("Yes")
    else:
        print("NO")        


# 위 코드와 다르게 중간의 순서가 틀렸는지 확인하는 체크절차 X
t = int(input())
# print(t)
for x in range(t):
    ps = input()
    count = 0
    
    for char in ps:
        if char == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            break
            
    if count == 0:
        print("YES")
    else:
        print("NO")


# 리스트를 활용한 풀이방법 #######################################################################
t = int(input())

for _ in range(t):
    ps = input()
    lst = []  # 괄호를 담을 바구니(스택)
    res = True
    
    for char in ps:
        if char == '(':
            # 열린 괄호는 일단 리스트트에 넣습니다.
            lst.append(char)
        else:
            # 닫힌 괄호 ')'를 만났을 때
            if len(lst) > 0:
                # 리스트트에 기다리는 '('가 있다면 하나 꺼냅니다.
                lst.pop()
            else:
                # 리스트트이 비어있다면 짝이 안 맞는 것이므로 실패!
                res = False
                break
    
    # 최종 판정: 중간에 오류가 없었고, 스택에 남은 괄호도 없어야 함
    if res and len(lst) == 0:
        print("YES")
    else:
        print("NO")        