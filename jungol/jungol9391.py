#시:h / 분:m 

h, m = map(int,input().split())
#print(h, m)

if h >= 12:  # AM/PM 판별 및 시간 변환
    result = "PM"  # PM의 값을 result 상자 안에 넣음음
    time = h - 12 if h > 12 else h 
else:
    result = "AM" # AM의 값을 result 상자 안에 넣음
    time = 12 if h == 0 else h
print(f"{time:02} : {m} {result}")    # :02 ; 앞 숫자를 두자리까지 출력하는 메소드드


#2 ###############################################################################
#02d ; d는 십진수로 출력하는 법

h, m = map(int,input().split())
ampm = "M"
if h>= 12:
    ampm = "PM"
else:
    ampm = "AM"

if h>        
