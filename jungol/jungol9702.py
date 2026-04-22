class Info:
    def __init__(self, name, age):
        self. name = name
        self.age = age
    def print(self):
        print(f"Name:{self.name}, Age:{self.age}")    

N = int(input())
name, age = map(int, input().split())
age = int(age) #qge는 숫자로 변환

p = []  # 사람이 많으니까 객체들을 담을 리스트 사용

for x in range(N): # N명 만큼 반복
    data = input().split()
    name = data[0]  # p리스트에 있는 이름/나이 정보를 인덱스 순서를 가지고 꺼낸다
    age =  int(data[1])  # 나이는 숫자로 비교해야 하니 int 변환

p1 = Info(name, age)   #Info객체 생성 
p.append()



##############################
N = int(input())    
#print(N)
lst = []

for x in range(N):
    name, age = input().split()
    print(name, age)


#2 ##################################################################################
class PersonAge:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

N = int(input())
# print(N)
people = [PersonAge(*input().split()) for i in range(N)]

people.sort(key=lambda x: x.age, reverse=True)

for p in people:
    print(f"Name:{p.name}, Age:{p.age}")


#3 ###############################################################################
class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"

lst = []
N = int(input())
for i in range(1, N+1):
    name, age = input().split()
    p = Profile(name, age)
    lst.append(p)

for i in range(N):
    print(sorted(lst, key=lambda x: x.age, reverse=True)[i])  #lambda함수;익명함수. 한번만 쓰고 다음에는 안쓴다다



