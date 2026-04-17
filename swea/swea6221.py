#승 -패
#가위 - 보  
#바위 - 가위
#보 - 바위
Man1 = input()
#print(Man1)
Man2 = input()
#print(Man2)

lst = ["가위", "바위", "보"]

if Man1 == Man2:
    print("Result : Draw")
elif (Man1 == "가위" and Man2 == "보") or \
    (Man1 == "바위" and Man2 == "가위") or \
    (Man1 == "보" and Man2 == "바위") :
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")


#2####################################################
L = ['가위','바위','보']
f = input()
s = input()
'가위' < '바위' , '바위' < '보', '보' < '가위'
if f == s:
    print('Result : Draw')
elif f > s:
    print('Result : Man1 Win!')
else:
    print('Resilt : Man2 Win!')