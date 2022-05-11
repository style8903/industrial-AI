# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np


#AND 함수
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#NAND 함수
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#OR 함수
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#XOR 함수
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


##########################################과제 내용###################################
def FULL_ADDER(x1, x2, c):
    s1 = XOR(x1, x2)
    sum_result = XOR(s1,c)

    c1 = AND(x1, x2)
    c2 = AND(s1, c)
    carry_result = OR(c1,c2)

    return sum_result, carry_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #사용자로 부터 값 입력 받음
    x1 = int(input('x1 : '))
    x2 = int(input('x2 : '))
    carry = int(input('carry : '))
    #결과 출력
    sum_result, carry_result = FULL_ADDER(x1,x2,carry)
    print('')
    print('Full Adder Result')
    print('x1\tx2\tc\tS\tC')
    print('{}\t{}\t{}\t{}\t{}'.format(x1,x2,carry,sum_result,carry_result))


    #전체 진리표 출력
    print('')
    print('----------------------')
    print('All Full Adder Chart')
    print('x1\tx2\tc\tS\tC')

    sum_result, carry_result = FULL_ADDER(0,0,0)
    print('0\t0\t0\t{}\t{}'.format(sum_result,carry_result))
    sum_result, carry_result = FULL_ADDER(0, 0, 1)
    print('0\t0\t1\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(0, 1, 0)
    print('0\t1\t0\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(0, 1, 1)
    print('0\t1\t1\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(1, 0, 0)
    print('1\t0\t0\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(1, 0, 1)
    print('1\t0\t1\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(1, 1, 0)
    print('1\t1\t0\t{}\t{}'.format(sum_result, carry_result))
    sum_result, carry_result = FULL_ADDER(1, 1, 1)
    print('1\t1\t1\t{}\t{}'.format(sum_result, carry_result))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
