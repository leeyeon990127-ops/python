# 함수사용
def words_str():
    print("Hello ")

N, M = map(int, input().split())

#print(N, M)

for i in range(N):
    words_str()
print()    
for x in range(M):
    words_str()


#2 range 사용(함수X)
N, M = map(int, input().split())
#print(N, M)

for i in range(N):
    print("Hello ")
print()
for i in range(M):
    print("Hello ")    