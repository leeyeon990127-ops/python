X, Y = map(float,input().split())
#print(X, Y)

if X >= 4.0 and Y >= 4.0:  # 모두 4.0이상
    print("A grade")  # 같은표현: out = "A grade"
elif X >= 3.0 and Y >= 3.0: # 모두 3.0 이상
    print("B grade")  # 같은표현: out = "B grade"
else:
    print("F grade")  # 같은표현: out = "F grade"
                      #print(out) 마지막에 out변수 출력


#2 match-case ##################################################################
X, Y = map(float, input().split())
# print(X, Y)
match (X, Y):
    case (X, Y) if X >= 4.0 and Y >= 4.0:
        print("A grade")
    case (X, Y) if X >= 3.0 and Y >= 3.0:
        print("B grade")
    case _: 
        print("F grade")
