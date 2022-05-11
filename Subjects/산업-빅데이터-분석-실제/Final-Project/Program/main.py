import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime as dt
warnings.filterwarnings("ignore", category=DeprecationWarning)

##목표 : 오전 8시~9시 환자수를 통해 당일 전체 환자수 예측
##      월요일 환자수 데이터를 통해 금주 전체 환자수 예측

#step 1 : 최초 데이터 셋 확인
print('-----------------------STEP1-------------------------')

data = pd.read_csv('m_db2.csv', sep=',')
data_1 = data.copy()
print(data_1.info())

print('-----------------------------------------------------')

#step 2 : 년도, 날짜, 시간 컬럼 추가
print('-----------------------STEP2-------------------------')

data_1['T_START'] = pd.to_datetime(data_1['T_START'])
data_1['T_END'] = pd.to_datetime(data_1['T_END'])
data_1['YEAR'] = data_1['T_END'].dt.year
data_1['MONTH'] = data_1['T_END'].dt.month
data_1['DAY'] = data_1['T_END'].dt.day
data_1['HOUR'] = data_1['T_END'].dt.hour
print(data_1.info())

print('-----------------------------------------------------')

#step 3 : 날짜 시간별 카운트를 위한 불필요 열 제거
print('-----------------------STEP3-------------------------')
data_1.dropna(axis=0)   #null값 제거
data_2 = data_1.drop(['T_NUMBER', 'P_START', 'P_END', 'T_START','T_END'],axis=1)
print(data_2.info())

print('-----------------------------------------------------')

#step 4: 비정상 데이터 제거
print('-----------------------STEP4-------------------------')

print(data_2.groupby('YEAR').count())
error_idx = data_2[data_2['YEAR'] == 1899].index
data_3 = data_2.drop(error_idx)
print(data_3.groupby('YEAR').count())

data_3.to_csv("final_data.csv")
print('-----------------------------------------------------')

#step 5 : 카운트 값 추가
print('-----------------------STEP5-------------------------')
# c_data['CNT'] = c_data['YEAR'].groupby()
# c_data['CNT'] = c_data.value_counts()
data = pd.read_csv('final_data2.csv', sep=',')
data_4 = data.copy()
data_4 = data_4.drop_duplicates(keep='first')
print(data_4.info)
data_4.to_csv("final_data3.csv")
print('-----------------------------------------------------')

#step 6 : 최종 전처리 데이터 확인
print('-----------------------STEP6-------------------------')
final_data = pd.read_csv('final_data4.csv', sep=',')
no_use_idx = final_data[final_data['HOUR'] != 8].index
final_data = final_data.drop(no_use_idx)
print(final_data.info)
print('-----------------------------------------------------')

#step 7 : numpy를 이용한 데이터 시각화
print('-----------------------STEP7-------------------------')
np_final_data = np.array(final_data)
x_data = np_final_data[:,4]
y_data = np_final_data[:,5]
plt.plot(x_data,y_data,'bo')
plt.xlabel('input')
plt.ylabel('output')
plt.show()
print('-----------------------------------------------------')

#step 8 : sklearn 선형 회귀를 통한 분석 및 예측
print('-----------------------STEP8-------------------------')

#train data 및 test data 나누기
x = final_data[['CNT']]
y = final_data[['TOTAL_CNT']]
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.85, test_size=0.15)
#예측 모델 생성
lr = LinearRegression()
lr.fit(x_train,y_train)

#정확도 측정
train_accuracy = lr.score(x_train,y_train)
print("lr train acc : {:.3f}".format(train_accuracy))
test_accuracy = lr.score(x_test,y_test)
print("lr test acc : {:.3f}".format(test_accuracy))

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

print('-----------------------------------------------------')

#step 9 : sklearn Ridge 모델을 통한 분석 및 예측
print('-----------------------STEP9-------------------------')

#예측 모델 생성
rdg = Ridge()
rdg.fit(x_train,y_train)
rdg01 = Ridge(alpha=0.1)
rdg01.fit(x_train,y_train)
rdg02 = Ridge(alpha=0.0001)
rdg02.fit(x_train,y_train)
rdg03 = Ridge(alpha=10000)
rdg03.fit(x_train,y_train)
#결과 확인
rdg_test_accuracy = rdg.score(x_test,y_test)
print("rdg test acc : {:.3f}".format(rdg_test_accuracy))
print('w : ',rdg.coef_,rdg.intercept_)
rdg01_test_accuracy = rdg01.score(x_test,y_test)
print("rdg01 test acc : {:.3f}".format(rdg01_test_accuracy))
print('w : ',rdg01.coef_,rdg01.intercept_)
rdg02_test_accuracy = rdg02.score(x_test,y_test)
print("rdg02 test acc : {:.3f}".format(rdg02_test_accuracy))
print('w : ',rdg02.coef_,rdg02.intercept_)
rdg03_test_accuracy = rdg03.score(x_test,y_test)
print("rdg03 test acc : {:.3f}".format(rdg03_test_accuracy))
print('w : ',rdg03.coef_,rdg03.intercept_)

print('-----------------------------------------------------')

#step 9 : sklearn Lasso 모델을 통한 분석 및 예측
print('-----------------------STEP10-------------------------')

#예측 모델 생성
lso = Lasso()
lso.fit(x_train,y_train)

lso01 = Lasso(alpha=0.01, max_iter=10000)
lso01.fit(x_train,y_train)

lso02 = Lasso(alpha=100, max_iter=10000)
lso02.fit(x_train,y_train)

#결과 확인
lso_test_accuracy = lso.score(x_test,y_test)
print("lso test acc : {:.3f}".format(lso_test_accuracy))
print('w : ',lso.coef_,lso.intercept_)

lso01_test_accuracy = lso01.score(x_test,y_test)
print("lso01 test acc : {:.3f}".format(lso01_test_accuracy))
print('w : ',lso01.coef_,lso01.intercept_)

lso02_test_accuracy = lso02.score(x_test,y_test)
print("lso02 test acc : {:.3f}".format(lso02_test_accuracy))
print('w : ',lso02.coef_,lso02.intercept_)

print('-----------------------------------------------------')


