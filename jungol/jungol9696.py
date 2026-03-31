class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        isold = 'child'
        if int(age) >= 18:
            isold = 'adult'
        else:
            isold = 'child'
        print(f"{name}({age}) : {isold} ")

for x in range(2):                            #두명의 데이터를 출력해야 하기때문에 2. 10명이미면 10
    name, age = input().split()
    obj = Person(name, age)
    obj.print()