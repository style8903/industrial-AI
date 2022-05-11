import numpy as np

#1
x_train = np.array([1., 2., 3., 4., 5., 6.])
y_train = np.array([9., 12., 15., 18., 21., 24.])

n_data = len(x_train)
epochs = 5000
learning_rate = 0.01
W = 0.0
b = 0.0

for i in range(epochs):
    hypothesis = x_train * W + b
    cost = np.sum((hypothesis - y_train)**2) / n_data
    gradient_w = np.sum((W * x_train - y_train + b)* 2 * x_train) / n_data
    gradient_b = np.sum((W * x_train - y_train + b)* 2) / n_data

    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

    if i % 100 == 0:
        print('Epoch ({:10d}/{:10d}) cost: {:10f}, W: {:10f}, b:{:10f}'.format(i, epochs, cost, W, b))

print('W: {:10f}'.format(W))
print('b: {:10f}'.format(b))
print('result : ')
print(x_train * W + b)


#2
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
df = pd.DataFrame(data=boston.data, columns = boston.feature_names)
df['price'] = boston.target
print(df)
print(df.isnull().sum())


#3
from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = datasets.fetch_california_housing()
x_data = dataset.data
y_data = dataset.target

x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.3)

estimator = LinearRegression()
estimator.fit(x_train, y_train)

y_predict = estimator.predict(x_train)
score = metrics.r2_score(y_train, y_predict)
print(score)

y_predict = estimator.predict(x_test)
score = metrics.r2_score(y_test, y_predict)
print(score)

#4
import mglearn
from sklearn.linear_model import Ridge
from sklearn import model_selection

X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=0)

ridge = Ridge().fit(X_train, y_train)
print("훈련 세트 점수 : {:.2f}".format(ridge.score(X_train, y_train)))
print("테스트 세트 점수 : {:.2f}".format(ridge.score(X_test, y_test)))

ridge10 = Ridge(alpha=10).fit(X_train, y_train)
print("훈련 세트 점수 : {:.2f}".format(ridge10.score(X_train, y_train)))
print("테스트 세트 점수 : {:.2f}".format(ridge10.score(X_test, y_test)))

ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
print("훈련 세트 점수 : {:.2f}".format(ridge01.score(X_train, y_train)))
print("테스트 세트 점수 : {:.2f}".format(ridge01.score(X_test, y_test)))

#5
from sklearn.linear_model import Lasso
lasso = Lasso().fit(X_train, y_train)
print("훈련 세트 점수 : {:.2f}".format(lasso.score(X_train, y_train)))
print("테스트 세트 점수 : {:.2f}".format(lasso.score(X_test, y_test)))
print("사용한 특성의 개수:", np.sum(lasso.coef_ != 0))
