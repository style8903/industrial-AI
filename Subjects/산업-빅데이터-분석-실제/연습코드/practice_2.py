#1
import datetime

print(7/3)
print(3**4)
print(7%3)
print(7//3)

#2
X = 15
print("{0}".format(X))
print("{0}".format(3/5))
print("{0}".format(X**3))
print("{0}".format(int(10.5)))
print("{0}".format(int(10.5)/int(8.5)))

#3
X = 10.5 * 4.7
print("{0}".format(X))
print("{0:.1f}".format(X))
print("{0:.3f}".format(X))

#4
x = int(input("정수 x = "))
y = int(input("정수 y = "))

print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x/y)
print("%d + %d = %d"% (x,y,x+y))
print("%d - %d = %d"% (x,y,x-y))
print("%d * %d = %d"% (x,y,x*y))
print("%d / %d = %d"% (x,y,x/y))

#5
current_datetime = datetime.today()
print("{0!s}".format(current_datetime))
print("{0!s}".format(current_datetime.year))
print("{0!s}".format(current_datetime.month))
print("{0!s}".format(current_datetime.day))
print("{0!s}".format(current_datetime.hour))
print("{0!s}".format(current_datetime.minute))
print("{0!s}".format(current_datetime.second))

#6
sum = 0
for data in [23, 45, 67, 43, 12]:
    sum += data
print("자료의 합 = ", sum)

score = [23, 45, 67, 43, 12]
sum = 0
for data in reversed(score):
    sum += data
print("자료의 합 = ", sum)