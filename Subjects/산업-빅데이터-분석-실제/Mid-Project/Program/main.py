import numpy as np
import pandas as pd
import warnings
import datetime as dt
warnings.filterwarnings("ignore", category=DeprecationWarning)

##목표 : 오전 8시~9시 환자수를 통해 당일 전체 환자수 예측
##      월요일 환자수 데이터를 통해 금주 전체 환자수 예측

#step 1 : 최초 데이터 셋 확인
data = pd.read_csv('m_db2.csv', sep=',')
c_data = data.copy()
np_data = np.array(c_data)

print(c_data.info())
print(c_data.head())
print('-----------------------------------------------------')
print('-----------------------------------------------------')

#step 2 : 년도, 날짜, 시간 컬럼 추가
c_data['T_START'] = pd.to_datetime(c_data['T_START'])
c_data['T_END'] = pd.to_datetime(c_data['T_END'])
c_data['YEAR'] = c_data['T_END'].dt.year
c_data['MONTH'] = c_data['T_END'].dt.month
c_data['DAY'] = c_data['T_END'].dt.day
c_data['WEEK'] = c_data['T_END'].dt.day_name()
c_data['HOUR'] = c_data['T_END'].dt.hour
c_data.dropna(axis=0)   #null값 제거
print(c_data.info())
print(c_data.head())
print('-----------------------------------------------------')
print('-----------------------------------------------------')

#step 3 : 날짜 시간별 카운트를 위한 불필요 열 제거
c_data = c_data.drop(['T_NUMBER', 'P_START', 'P_END', 'T_START','T_END'],axis=1)
print(c_data.info())
print(c_data.head())
print('-----------------------------------------------------')
print('-----------------------------------------------------')

#step 4 : 중복값 제거 후 중복값에 대한 컬럼 추가 및 해당 컬럼에 count 개수 데이터 추가
process_data = c_data.drop_duplicates(keep='first')
print(process_data)
print(process_data.head())
print('-----------------------------------------------------')
print('-----------------------------------------------------')

# c_data['COUNT'] = c_data.groupby(['YEAR','MONTH','DAY','HOUR']).count()
# print(c_data.info)
# print(c_data.head())
# print('-----------------------------------------------------')
# print('-----------------------------------------------------')


# data_2021_9 = c_data[(c_data['YEAR'] == 2022) & (c_data['MONTH'] == 9) & (c_data['DAY'] == 7)].count()
# print(data_2021_9)