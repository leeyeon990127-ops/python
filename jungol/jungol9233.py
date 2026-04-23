a = int(input())
#print(a)
b = int(input())
#print(b)

if a >= 3 and b >= 3:   # 좌항과 우항의 값이 모두 참 : and
    print("High") 
elif a >= 3 or b >= 3:  # 
    print("Mid")
else:
    print("Low")    

#2 - match -case 문######################################################
a = int(input())
b = int(input())
# print(a, b)
match (a >= 3, b >= 3):
    case (True, True):
        print("High")
    case (True, False) | (False, True):  # |: or 연산의미
        print("Mid")
    case _:
        print("Low")