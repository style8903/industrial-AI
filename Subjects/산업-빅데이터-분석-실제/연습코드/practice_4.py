import numpy as np
import time

#1
n = 1000
m = 5000

X = np.random.rand(n,m)
W = np.random.rand(n,1)
Z = np.zeros(1,m)

#2
start_time = time.time()

for i in range(X.shape[1]):
    for j in range(X.shape[0]):
        Z[0][i] += W[j]*X[j][i]

end_time = time.time()
print("반복문 이용 실행시간: ", (end_time - start_time)*1000, "ms")

#3
x = np.float32(1.0)
print(x)
y = np.int_([1,2,4])
print(y)
x = np.array([2,3,1,0])
print(x)

#4
print(np.zeros((2,3)))
print(np.arange(10))
print(np.arange(2,10, dtype = float))
print(np.linspace(1.,4.,6))

#5
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a == b)
print(a > b)

c = np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))

a = np.array([1,1,0,0], dtype=bool)
b = np.array([1,0,1,0], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

#6
x = np.array([1,2,3,4])
print(np.sum(x))
print(x.sum())

x = np.array([[1,1],[2,2]])
print(x)
print(x.sum(axis= 0))
print(x.sum(axis= 1))

#7
x = np.random.rand(2,2,2)
print(x.sum(axis=2))
print(x.min())
print(x.max())
print(x.mean())
print(np.median(x))