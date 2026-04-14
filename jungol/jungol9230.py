T = int(input())
#print(T)

if T >= 12:
    print("PM")
else:
    print("AM")


#2-----------------------------
time = int(input())

res = ""    #변수선언
if time < 12:
    res = "AM"
else: 
    res = "PM"
print(res)      


#3----------------------------------
hour = int(input())
# print(hour)
is_pm = bool(hour // 12)
print("PM" if is_pm else "AM")
