import matplotlib.pyplot as plt
import numpy as np

#1
N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
plt.plot(x1, y, 'o')
plt.plot(x2, y + 0.5, 'o')
plt.ylim([-0.5, 1])
plt.show()

#2
x = np.linspace(0.3, 3, 100, endpoint=True)
y = np.logspace(0.3, 3, num= 100)
plt.plot(x, y, 'o')
plt.show()

#3
nx, ny = (2,3)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xx, yy = np.meshgrid(x, y)
print("X : ", x, "Y : ", y)
print("XX : ", xx,"YY : ", yy)

#4
nx, ny = (10, 10)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2 + yy**2)
h = plt.contourf(x, y, z)
plt.show()

#5
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x,y)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x, y, z)
plt.show()

#6
A = np.arange(8)
print(A)
B = A.reshape(2,4)
A.ndim
print(A.shape)
B.ndim
print(B)
C = B.reshape(4,2)
print(C)
D = B.reshape(2,2,2)
print(D)

#7
print(np.dot(2,5))
print(np.dot[1,2], [3,4])
A = np.array([[1,2], [3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(np.matmul(A,B))
L = np.array([[1,0,0],[1,1,0],[2, -4.5, 1]])
b = [7, 13, 5]
y = np.linalg.solve(L,b)
print(y)