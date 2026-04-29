#버블소트(버블정렬)
# 왼쪽과 오른쪽을 비교 -> 왼쪽이 크면 자리 바꿈 / 오른쪽이 크면 그대로 둠
#스왑

n = int(input())
lst = list(map(int,input().split()))

def bubble_sort(lst):
        lengh = len(lst)

        for i in range(n-1):
            for j in range(0, n-1-i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j] #두 값의 위치를 바꿈(swap)
            print(*(lst))       
bubble_sort(lst)             

# --- 스왑 시작 ---
temp = lst[j]
lst[j] = lst[j + 1]
lst[j + 1] = temp
# --- 스왑 끝 ---


#2 함수를 이용하지 않은 ################################################################
N = int(input())

hap=list(map(int,input().split()))

for i in range(N-1):
    for j in range(1,N-i):
        if hap[j-1] > hap[j] :
            hap[j-1], hap[j] = hap[j], hap[j-1]
    print(hap)



#3 ##############################################################################
#bubble sort
N = int(input())
lst = list(map(int, input().split()))

# print(lst)
isSorted = True

while isSorted:
    isSorted = False
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
            isSorted = True
    if isSorted == True:
        print(lst)    