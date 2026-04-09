K = int(input())
#print(K)
lst  = list(map(int,input().split()))

def k_diff(param):
    d = abs(K - param )  #절대값을 구하는 함수
    return d

for i in range(3):
   ret = k_diff(lst[i])
   print(ret)