text = "abcde"
print(*text[::2])

#2
inp = input()
for i in range(len(inp)):
    if i%2 == 0:
        print(inp[i], end=' ')