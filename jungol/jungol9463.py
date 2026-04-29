# 버블소트(버블정렬)
# 왼쪽과 오른쪽을 비교 -> 왼쪽이 크면 자리 바꿈 / 오른쪽이 크면 그대로 둠
# 스왑

lst = list(map(int, input().split()))

n = len(lst)

for i in range(n-1):
    for j in range(n-1-i):  
        if lst[j] < lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]  #스왑 a, b = b, a
    print(*(lst))   # *언패킹 출력     

#-1의 의미: 정렬이 완료된 구역 제외
# 버블정렬은 한단계가 끝날떄마다 특정 값 하나가 자기 자리를 찾게된다
#내림차순 정렬 시: 1단계가 끝나면 가장 작은 값이 맨뒤로 가고 2단계가 끝나면 그다음 작은 값이 뒤에서 두번째 자리에 고정된다


#2 함수 선언 : 재귀함수 #################################################################################
def bubble_sort(arr, n):
    if n == 1:
        return

    for j in range(len(arr) - (len(arr) - n + 1)):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    print(*(arr))
    
    bubble_sort(arr, n - 1)

nums = list(map(int, input().split()))
bubble_sort(nums, len(nums))
#재귀함수 ;함수 바로 뒤에는 return 값이 있다다