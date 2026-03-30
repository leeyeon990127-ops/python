a, b = map(int, input().split())
#print(a, b)

if a > b:
    print(a)
else:
    print(b)


#2---------------------------------------    
a, b = map(int, input().split())
c = [a,b]     #[ ] :리스트

print(max(c))   # = print(max(a, b))