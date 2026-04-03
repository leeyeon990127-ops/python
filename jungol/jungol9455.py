#lth = l

l = int(input())
#print(l)
#N = float(input()) 변수 선언을 하지 않고도 그냥

#방법1
def get_area_circle(lth):
    area = lth * lth * 3.14   #area :문제에서 말하는 구하라는 원의 넓이
    print(f"{area:.2f}")

get_area_circle(l)


#방법2
def get_area_circle(lth):
    area = lth * lth * 3.14 
    return area

r = int(input())
#print(r)
ret = get_area_circle(r)
#print(ret)
print("%.2f" % ret)