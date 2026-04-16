W = float(input())
#print(W)

if W <= 50.80:
    print("Flyweight")
elif W <= 61.23:
    print("Lightweight")
elif W <= 72.57:
    print("Middleweight")
elif W <= 88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")