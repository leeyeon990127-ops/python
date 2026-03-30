class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

name, age = input().split()
#print(name, age)
p1 = Person(name, age)
p1.print()