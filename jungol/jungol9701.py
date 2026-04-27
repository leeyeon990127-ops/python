class Operation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Operation (self.x + other.x , self.y + other.y)
    def __sub__(self, other):
        #return f"sub = ({self.x - other.x}, {self.y - other.y})"
        #위 코드가 안되는 이유 ; 글자뭉치 String이 되었고 그래서 숫자로 계산이 불가능
        return Operation (self.x - other.x, self.y - other.y)
    def __str__(self):    
        #return f"center = ({self.x:-1f}, {self.y:-1f})" 
        return f"({self.x:.1f}, {self.y:.1f})"  
                        # : (콜론): "지금부터 이 변수의 모양(형식)을 지정하겠다"라는 신호입니다.
                        #.1 (점과 숫자): "소수점 아래 첫 번째 자리까지"만 보여달라는 뜻입니다. (만약 .2라면 두 번째 자리까지 보여줍니다.)
                        # f (타입): "이 데이터는 실수(float) 형태다"라는 것을 알려줍니다.

x1, y1 = map(float,input().split())
o1 = Operation(x1, y1)
x2, y2 = map(float,input().split())
o2 = Operation(x2, y2)

hap = o1 + o2
cha = o1 - o2
center = Operation(hap.x / 2, hap.y / 2)

print(f"add = {hap}")
print(f"sub = {cha}")
print(f"center = {center}")



#2 #########################################################################################
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)    
    def __sub__(self, other):
        return Point (self.x - other.x, self.y - other.y)
    
    def __truediv__(self, other):
        return f"({self.x / other.x, self.y / other.y})"

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"  
   

lst = []
for i in range(2):
    lst[i].print()

retp1 = lst[0] + lst[1]
retp1.print()
print(retp1)

print("add= ", end='')
retp2 = lst[0] - lst[1]
print(retp2)

print("center = ", end="")
retp3 = retp1 / Point(2.0, 2.0)
print(retp3)
