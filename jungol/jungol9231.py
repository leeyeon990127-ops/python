#if elif else
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B') 
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:    
    print('F')

#2---------------------------------
score=int(input())

match score // 10:   #//:몫
    case 10 | 9:
        print('A')
    case 8:
        print("B")
    case 7:
        print("C")
    case 6:
        print("D")
    case _:   # default와 같은 
        print('F')