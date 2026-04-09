N = int(input())
#print(N)

def Numbers():
    if N > 0:
        return 'positive'
    elif N < 0:
        return 'negative'
    else:
        return 'zero'
print(Numbers())          #함수 호출 및 결과 저장

#2------------------------------------
inp = int(input())

def get_integer(p):
    ret = ""
    if p>0:
        ret = "positive"
    elif p<0:
        ret = "negative"   
    else:
        ret = "zero"   

    return ret
    
#3----------------------------------
r = get_integer()       

def check_number(n):
    mapping = {
        (n > 0): 'positive',
        (n < 0): 'negative',
        (n == 0): 'zero'
    }
    return mapping[True]

num = int(input())
# print(num)
print(check_number(num))
