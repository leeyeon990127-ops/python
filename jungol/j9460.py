a, b = map (int,input().split())
#print(a, b)

def Sentance():
    if a == 10 or b == 5:
        return f"함수 내부: a = 10, b = 5"
    else:
        return f"함수 외부: a = 5, b = 10"
        
Sentance()

#for x in range(4):

