# ?0 *5
# ?1 *4
# ?2 *3
# ?3 *2
# ?4 *1
# -> 공백이 먼저 출력되고 일정하게 감소

N = int(input())
#print(N)

for x in range(N):  # 행
    # ? for 
    for y in range(x): # 열/ 공백을 출력
        print(" ", end=" ")
    # * for
    for x in range(N-x, 0, -1): # 열/ 별을 출력
        print("*", end=" ")   
    print()

#2 #########################################################################
n = int(input())
for i in range(n,0,-1):
    print(f"{'*'*i:>{n}}")  #우측정렬 :>{}
  

