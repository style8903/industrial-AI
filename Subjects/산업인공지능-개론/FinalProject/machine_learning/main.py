import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
from pandas.io.parsers import read_csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#############최초 데이터 확인##############
data = read_csv('project_db.csv', sep=',')
xy = np.array(data)
#print(xy)
x_data = xy[:,2]
print(x_data)
y_data = xy[:,3]
print(y_data)
plt.plot(x_data,y_data,'bo')
plt.xlabel('input')
plt.ylabel('output')
plt.show()

for i in range(0,len(x_data)):
    if x_data[i] < 50 and y_data[i] > 750:
        print(i)

#########극단치 제거###############
data = read_csv('project_db2.csv', sep=',')
xy = np.array(data)
#print(xy)
x_data = xy[:,2]
# print(x_data)
y_data = xy[:,3]
# print(y_data)
# plt.plot(x_data,y_data,'bo')
# plt.xlabel('input')
# plt.ylabel('output')
# plt.show()



###############TensorFlow 활용 오차 제곱합으로 회귀선 구해보기##################
w = tf.Variable(random.random())
b = tf.Variable(random.random())

def cal_loss():
    result = w * x_data + b
    loss = tf.reduce_mean((y_data - result)**2)
    return loss

#linear regression 0.05설정
optimizer = tf.optimizers.Adam(lr=0.05)

for i in range(10000):
  # 오차 제곱 평균 최소화
  optimizer.minimize(cal_loss, var_list=[w,b])
  #가중치 및 bias, loss 구하기
  if i % 100 == 99:
    print(i, 'a:', w.numpy(), 'b:', b.numpy(), 'loss:', cal_loss().numpy())

line_x = np.arange(min(x_data), max(x_data), 0.01)
line_y = w * line_x + b

# 회귀선 그리기
plt.plot(line_x, line_y, 'r-')
plt.plot(x_data, y_data, 'bo')
plt.xlabel('input')
plt.ylabel('output')
plt.show()



#######################sklearn 사용######################
#train data 및 test data 나누기
x = data[['input_count']]
y = data[['total_count']]
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8, test_size=0.2)
#예측 모델 생성
lr = LinearRegression()
lr.fit(x_train,y_train)

#정확도 측정
accuracy = lr.score(x_train,y_train)
print(accuracy)

#예측값 구하기
y_predicted = lr.predict(x_test)
mse = mean_squared_error(y_test, y_predicted)
print(mse)
print('w : ',lr.coef_,lr.intercept_)

#산포도 구해보기
plt.scatter(y_test,y_predicted, alpha=0.5)
plt.xlabel('y_test')
plt.ylabel('y_predicted')
plt.show()




