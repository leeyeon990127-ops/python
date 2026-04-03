a = int(input())
#print(a) #9, 14

if a < 13:
    print("Elementary School")
else:
    print("Middle School")

#2-----------------
age = int(input())
# print(age)
schools = ["Elementary School", "Middle School"]
print(schools[age >= 13])

#3-----------------------
print("Middle School" if int(input()) >= 13 else "Elementary School") 