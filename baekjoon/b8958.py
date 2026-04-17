#OX퀴즈 문제 

T = int(input())
#print(a)
for x in range(T):
    str = input()    #스트링 변수에 OOXXOXXOOO가 들어있는것
    #print(str)
    
    sum = 0  #합계값의 들어가는 변수
    score = 1 #
    for i in str:
        #print(i, end=" ")
        if i == '0':
            sum += score
            score =+ 1
        else:    
            score = 1
    print(sum)        


#2 ##########################################################
T = int(input())

for i in range(T):
    ox_res = input()
    total_score = 0
    current_line = 0
    
    for char in ox_res:
        match char:
            case 'O':
                current_line += 1
                total_score += current_line
            case 'X':
                current_line = 0
            case _:
                pass
    print(total_score)