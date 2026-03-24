print("*   *")
print(" * *")
print("  *")

print("Apple Banana Carrot")
print('Apple', 'Banana', 'Carrot', sep=',')


letter = "how are You?"
print(letter.lower())
print(letter.upper())
print(letter.capitalize())
print(letter.swapcase())
print(letter.split())

str1 = letter. split()
print(str1[0].capitalize())
print(str1[1].capitalize())
print(str1[2].capitalize())


letter = "how are You?"
print(letter.count('how'))
leteer = "how are you"
print(letter.count('0'))

s = '나도고등학교'
print(s.startswith('나도'))
print(s.endswith('초등학교'))
print(s.endswith('고등학교'))

s2 = '...나도고등학교...'
print(s2.strip(' '))

s3 = '.,.나도고등학교.,.'
print(s3.strip('.'))

s4 = '나도고등학교'
print(s4.replace('고등학교', '고교'))

s5 = '나도고교너도고교'
print(s5.replace('고교', '고등학교'))

s = '나도고등학교'
print(s.find('학교'))
print(s.find('너도'))
print(s.center(10,'-'))
