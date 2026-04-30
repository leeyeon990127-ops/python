'''코딩테스트입문-분수의덧셈'''
#9/2 + 1/3 = 
#27 + 2 
#=> 29/6


#def solution(numer1, denom1, numer2, denom2):
#    top =  (numer1 * denom2) + (numer2 * denom1 ) # 분자
#    down = denom1 * denom2                        # 분모
    
    
#########################################################################################
#2 math 라이브러리
import math

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = math.gcd(numer, denom)  # gcd; 최대공약수를 구하는 
    numer //= g
    denom //= g
    return [numer, denom]    


#3 
def solution(denum1, num1, denum2, num2):
    answer = []    
    a = 0
    b = 0

    a = (denum1 * num2) + (denum2 * num1)  
    b = num2 * num1
    for j in range(1, 1000):
        for i in range(1, 1000):
            if (a % i) == 0 and (b % i) == 0:
                a = a / i
                b = b / i
        answer = [a, b]

    return answer   