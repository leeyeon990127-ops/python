a, b = input().split()
#print(a, b)

def func_name():
    print(f"함수 내부: a = {b}, b = {a}")
    print(f"함수 외부: a = {a}, b = {b}")
    print(f"함수 내부: a = {b}, b = {a}")
    print(f"함수 외부: a = {b}, b = {a}")
func_name()

#2 지역변수와 전역변수
a, b = input().split()
#print(a, b)


def change_loc(pa, pb):
    a, b = pb, pa
    print(f"함수 내부: a = {a}, b = {b}")

change_loc(a, b)
print(f"함수 외부: a = {a}, b = {b}") 

change_loc(a, b)
print(f"함수 외부: a = {b}, b = {a}")


#2 ##############################################################################
def switch(a, b):
    a, b = b, a
    return f"함수 내부: a = {a}, b = {b}"

a, b = map(int,input().split())

change = switch(a, b)

print(change)
print(f"함수 외부: a = {a}, b = {b}")
a, b = b, a
print(change)
print(f"함수 외부: a = {a}, b = {b}")