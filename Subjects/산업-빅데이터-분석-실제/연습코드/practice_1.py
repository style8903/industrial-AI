#1
i = 10
j = 40
print(i, j, i+j)

#2
message = "안녕하세요. \n 환영합니다."
string1 = input("문자입력 = ")
print(message)

#3
str = "I eat %d apples." % 3
print(str)

str = "I eat %s apples." % "five"
print(str)

number = 10
day = "three"
str = "a = %d b = %s" %(number, day)
print(str)

#4
str1 = "안녕하세요"
str2 = "김성웅입니다."
print(str1 + str2)

print("hello" * 2)
print(str1*2)

#5
str = "Hello world"
print(str[0])
print(str[-1])
print(str[0:5])
print(str[:5])
print(str[6:11])
print(str[6:])

#6
str1 = "This is Python Program"
print(str1.upper())
print(str1.lower())
print(str1.count("is"))
print(len(str1))
print(str1.find('P'))
print(str1.index('T'))

ch = "충북"
str = "대학교"
"".join(str),"-".join(str),print(ch.join(str))