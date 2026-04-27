#::-1
word = "madam"

if word == word[::-1]:
    print(f"{word} \n입력하신 단어는 회문(Palindrome)입니다.")

#2 #########################################################################################
str1 = str(input())
str2 =''.join(reversed(str1))
if str1 == str2:
   print(str1,"\n입력하신 단어는 회문(Palindrome)입니다.")