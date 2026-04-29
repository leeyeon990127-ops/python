#프로그래머스-코딩테스트연습-완전탐색-모의고사

def solution(answers):
    p1 = [1, 2, 3, 4, 5]                  # 5개씩 반복
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]         # 8개씩 반복
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # 10개씩 반복
    
    scores = [0, 0, 0] # 점수를 저장할 리스트.인덱스 순서로 사람들의 순서로 들어감

    for i in range(len(answers)):
        answers = 
        if i % 
    
    
#2 ##################################################################
def solution(answers):
    # print(answers)
    # print(len(answers))

    sp1 = [1, 2, 3, 4, 5]
    sp2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        if answers[i] == sp1[i % len(sp1)]:
            score1 += 1
        if answers[i] == sp2[i % len(sp2)]:
            score2 += 1
        if answers[i] == sp3[i % len(sp3)]:
            score3 += 1

    print(score1, score2, score3)
    maxScore = max(score1, score2, score3)
    answer = []
    if maxScore == score1:
        answer.append(1)
    if maxScore == score2:
        answer.append(2)
    if maxScore == score3:
        answer.append(3)

    return answer

res = solution(ans)
print(res)


