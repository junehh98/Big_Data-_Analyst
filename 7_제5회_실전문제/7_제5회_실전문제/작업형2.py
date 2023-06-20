# -*- coding: utf-8 -*-
"""
################################################
# Q3. 작업형2(40점) : 데이터 모형 구축 & 평가 
################################################

   중고차 가격(price) 예측 모델을 개발하고, 개발한 모델을 기반하여 
   평가용 데이터를 이용하여 중고차 가격의 예측 결과를 아래 지시된 
   형식의 csv 파일로 생성하여 제출하시오.
       ​    price_pred
     1           15100
     2           6700 
     3           7280
     4           24640
                 :

 (유의사항)
  성능이 우수한 예측모델을 구하기 위해서 적절한 데이터 전처리, 
  Feature Engineering(결측치 처리, 이상치 처리, 변수변환, 스케일링, 차원축소), 
  분류알고리즘 선택, 모형 알상블 등이 수반되어야 한다.
  
 제출 : result.to_csv('수험번호.csv', index = False)
"""

import pandas as pd
path = r'C:\ITWILL\7_BigGisa\7_제5회_실전문제\data'
x_train = pd.read_csv(path +'/Train.csv') # 훈련셋 : X + y변수  
x_test = pd.read_csv(path +'/Test.csv') # 평가셋 X변수
y = x_train['price']

x_train.info()
'''
RangeIndex: 12576 entries, 0 to 12575
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   model         12576 non-null  object 모델명 : 제외 
 1   year          12576 non-null  int64   생산연도
 2   price         12576 non-null  int64  자동차 가격
 3   transmission  12576 non-null  object 엔진변속기
 4   mileage       12576 non-null  int64  주행한 마일수
 5   fuelType      12576 non-null  object 휘발유,라이브리드,전기,기타
 6   tax           12576 non-null  int64  연간 세금 
 7   mpg           12576 non-null  float64 갤런당 마일
 8   engineSize    12576 non-null  float64 자동차엔진크기 
''' 
 


### 단계0. 변수 탐색 : 결측치, 이상치, 인코딩, 스케일링 확인  
x_train_drop = x_train.drop(columns= ['model', 'price'])
x_test_drop = x_test.drop(columns='model')

x_train_drop['transmission'].value_counts()
x_train_drop['fuelType'].value_counts()

x_train_drop.isnull().sum()
x_test_drop.isnull().sum()

### 단계1. 데이터 전처리 & 특징공학  
from sklearn.preprocessing import StandardScaler # 회귀모델에서 X변수 스케일링
x_train_drop.columns

# 수치형 변수 스케일링
x_train_drop[['year','mileage', 'tax', 'mpg', 'engineSize']] \
    = StandardScaler().fit_transform(x_train_drop[['year','mileage', 'tax', 'mpg', 'engineSize']])
    
    
x_test_drop[['year','mileage', 'tax', 'mpg', 'engineSize']] \
    = StandardScaler().fit_transform(x_test_drop[['year','mileage', 'tax', 'mpg', 'engineSize']])

# 범주형 변수 인코딩
x_train_drop = pd.get_dummies(x_train_drop)
x_test_drop = pd.get_dummies(x_test_drop)

x_test_drop = x_test_drop[x_train_drop.columns]



### 단계2. 훈련셋/검증셋 나누기
from sklearn.model_selection import train_test_split 
x_train, x_val, y_train, y_val = train_test_split(x_train_drop, y,
                                                  test_size = 0.3,
                                                  random_state=1)



### 단계3. 사용할 모델 정하기 
from sklearn.ensemble import RandomForestRegressor # 회귀트리 
model = RandomForestRegressor(n_estimators = 1000,
                              max_depth = 150,
                              max_features=50,
                              random_state = 1)

model.fit(x_train, y_train)
model.score(x_train, y_train)
model.score(x_val, y_val)



### 단계4. best 파라미터 찾기 
from sklearn.model_selection import GridSearchCV




### 단계5. test 데이터 예측값 구하기
train_predict = model.predict(x_train)
val_predict = model.predict(x_val)

import sklearn
import numpy as np
from sklearn.metrics import mean_squared_error
# 평가척도 rmse값으로 해보기

print('train_score :', np.sqrt(mean_squared_error(y_train, train_predict)))
print('val_score :', np.sqrt(mean_squared_error(y_val, val_predict)))

test_preidct = model.predict(x_test_drop)
test_preidct


### 단계6. 예측값 csv 파일 작성 & 제출
pd.DataFrame({'model': x_test.model, 'test_price': test_preidct}).to_csv('003000000.csv', index=False)

result = pd.read_csv('C:/ITWILL/7_BigGisa/7_제5회_실전문제/7_제5회_실전문제/003000000.csv')
result
