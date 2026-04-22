# while 무한루프. 입력받는 값의 횟수가 정해져 있지 않음
while True:
    n = int(input())

    if n == 1:
        print("one")
    elif n == 2:
        print("two")
    elif n == 3:
        print("three")
    else:
        break

# match - case문
while True:
    n = int(input())
    match n:
        case 1: print("one")
        case 2: print("two")
        case 3: print("three")
        case _: break    

