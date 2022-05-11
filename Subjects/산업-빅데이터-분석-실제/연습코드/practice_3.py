#1
x = int(input("정수 x = "))

if(x % 2 == 1):
    print("홀수입니다.")
else:
    print("짝수입니다.")


#2
score = int(input("점수 = "))

if(score >= 90):
    print("A학점")
elif(score >= 80):
    print("B학점")
elif(score >= 70):
    print("C학점")
elif(score >= 60):
    print("D학점")
else: print("F학점")

#3
sum = 0
for i in range(1,101):
    sum += i
print("1+2+...+100", sum)
print("1+2+...+100"+str(sum))

#4
sum = 0
i = 1
while(i <= 100):
    sum += i
    i += 1
print("1+2+...+100 =", sum)

sum = 0
i = 1
while(i <= 100):
    sum += i
    i *= 2
print("1+2+4+...+64 = ",sum)

#5
import random
ans = random.randrange(1,101,1)
num = -1
t_cnt = 0
print("1~100 숫자 Up & Down 게임을 시작합니다.")
print("-----------------------------------")
while(ans != num):
    num = int(input("1~100 사이의 숫자를 입력하세요 : "))
    if(num > ans):
        print("Down")
    elif(num < ans):
        print("Up")
    t_cnt += 1

print("-----------------------------------")
print(t_cnt, "번 만에 정답을 맞추었습니다.")