#text = "pineapple"
#print(text)
#reversed_text = "".join(reversed(text))  ------java때 다시 
#print(reversed_text)



#2------
N = input()
print(N)
for x in range(len(N)-1, -1, -1):
    print(N[x], end= ' ')

#3-----------------------
a = input()
print(a[::-1]) # 역순으로(-1)
#::는 주로 리스트나 문자열을 자를 때(Slicing) 사용하며, 
#**"어떤 간격으로 가져올 것인가"**를 결정합니다.

#기본 구조는 [시작:끝:단계]인데, 
#::를 쓰면 시작과 끝을 생략하고 **단계(Step)**만 지정하겠다는 뜻입니다.