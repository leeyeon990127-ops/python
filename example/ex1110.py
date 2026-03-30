f = open('list.txt', 'r', encoding='utf-8' )
for line in f:
    print(line, end='')
f.close()