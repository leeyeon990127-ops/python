for X in range(1, 5001):
    print(X,end =' ')

#range(1, 10, 2) ; 1이상, 10 미만 2만큼 증가


#2---------------
[print(i, end=" ") for i in range(1, 5001)]

#3----------------
print(" ".join(f"{x}" for x in range(1, 5001)))