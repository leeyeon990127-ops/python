class Person():
    def __init__(self, tall, weight):
        self.tall = tall
        self.weight = weight
    def print_var():
        print(f"키: {self.tall}, 몸무게: {self.weight:.1f}")   #":d"는 정수를 출력하라, ":f"는 실수를 출력하라 ,.이 


tall, weight= map(float, input("당신의 키와 몸무게를 입력하세요").split())
print(tall, weight)
P1 = Person(tall, weight) #객체 생성
P1.print_var()

tall, weight= map(float, input("당신의 키와 몸무게를 입력하세요").split())
print(tall, weight)
P2 = Person(tall, weight)
P2.print_var()

#---------------------------------------------------------------------------
class Person:
    def __init__(self, cm, kg):
        self.cm = int(cm)
        self.kg = kg
    def __add__(self, other):
        # print("plus 키:", self.cm + other.cm, ", 몸무게: ", self.kg + other.kg)
        print(f"plus 키: {self.cm + other.cm}, 몸무게: {self.kg + other.kg}")
    def __sub__(self, other):
        print("minus 키:", abs(self.cm - other.cm), end='')
        print(f", 몸무게: {abs(p1.kg - p2.kg):.1f}")
    def __truediv__(self, other):
        print(f"avg 키: {int((self.cm + other.cm)/2)}, 몸무게: {((self.kg + other.kg)/2):.1f}")
    def __str__(self):
        return  f"키: {self.cm}, 몸무게: {self.kg:.1f}"
        
cm, kg = map(float, input("당신의 키와 몸무게를 입력하세요.").split())
p1 = Person(cm, kg)

cm, kg = map(float, input("친구의 키와 몸무게를 입력하세요.").split())
p2 = Person(cm, kg)

print("my", p1)
print("friend", p2)
p1 + p2
p1 - p2
p1 / p2