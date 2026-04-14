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


