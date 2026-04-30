'''프로그래머스-코딩테스트연습-코딩테스트입문-몫구하기'''
def solution(num1, num2):
    answer = num1 // num2
    return answer

#2
import math 

def solution(num1, num2):
    answer = math.trunc(num1 // num2)
    return answer    

#3
def solution(num1, num2):
    answer = (int)(num1 / num2)
    return answer   