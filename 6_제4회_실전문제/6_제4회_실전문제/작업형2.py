# -*- coding: utf-8 -*-
"""
################################################
# Q3. 작업형2(40점) : 데이터 모형 구축 & 평가 
################################################

 세분화 시장(Segmentation) 예측 모델을 개발하고, 개발한 모델을 기반하여 
 평가용 데이터를 이용하여 고객이 속할 세분화 시장의 예측 결과를 아래 지시된 
 형식의 csv 파일로 생성하여 제출하시오.

       ​Segmentation_pred
     1           2
     2           1 
     3           2
     4           4
                 :

 (유의사항)
  성능이 우수한 예측모델을 구하기 위해서 적절한 데이터 전처리, 
  Feature Engineering(결측치 처리, 이상치 처리, 변수변환, 스케일링, 차원축소), 
  분류알고리즘 선택, 모형 알상블 등이 수반되어야 한다.
  
 제출 : result.to_csv('수험번호.csv', index = False)
"""

# 데이터 파일 읽기 
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\6_제4회_실전문제\data'
x_train = pd.read_csv(path +'/Train.csv') # 훈련셋   
x_test = pd.read_csv(path +'/Test.csv') # 평가셋 
y_train = x_train['Segmentation']


### 단계0. 변수 탐색 
# x_train 컬럼 drop
# 범주형 변수들 encoding, y도 해야함
 
x_train.info() # segmentation 컬럼 drop, 범주형 인코딩
x_test.info() # object컬럼 인코딩
y_train # 인코딩



### 단계1. 데이터 전처리 & 특징공학  
x_train.isnull().sum()
x_test.isnull().sum()


x_train_drop= x_train.drop(columns='Segmentation')
x_test_drop = x_test
y = y_train
'''
x_train_num = x_train[['Age','Work_Experience','Family_Size']]
x_train_obj = x_train[['Gender','Ever_Married','Graduated','Profession', 'Spending_Score']]


x_test_num = x_test[['Age','Work_Experience','Family_Size']]
x_test_obj = x_test[['Gender','Ever_Married','Graduated','Profession', 'Spending_Score']]
'''


from sklearn.preprocessing import MinMaxScaler, LabelEncoder
x_train_drop[['Age','Work_Experience','Family_Size']] = MinMaxScaler().fit_transform(x_train_drop[['Age','Work_Experience','Family_Size']])
x_test_drop[['Age','Work_Experience','Family_Size']] = MinMaxScaler().fit_transform(x_test_drop[['Age','Work_Experience','Family_Size']])


x_train_drop['Gender'] = LabelEncoder().fit_transform(x_train_drop['Gender'])
x_train_drop['Ever_Married'] = LabelEncoder().fit_transform(x_train_drop['Ever_Married'])
x_train_drop['Graduated'] = LabelEncoder().fit_transform(x_train_drop['Graduated'])
x_train_drop['Profession'] = LabelEncoder().fit_transform(x_train_drop['Profession'])
x_train_drop['Spending_Score'] = LabelEncoder().fit_transform(x_train_drop['Spending_Score'])


x_test_drop['Gender'] = LabelEncoder().fit_transform(x_test_drop['Gender'])
x_test_drop['Ever_Married'] = LabelEncoder().fit_transform(x_test_drop['Ever_Married'])
x_test_drop['Graduated'] = LabelEncoder().fit_transform(x_test_drop['Graduated'])
x_test_drop['Profession'] = LabelEncoder().fit_transform(x_test_drop['Profession'])
x_test_drop['Spending_Score'] = LabelEncoder().fit_transform(x_test_drop['Spending_Score'])



import sklearn
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
'''
x_train_drop['Gender'] = LabelEncoder().fit_transform(x_train_drop['Gender'])
x_train_drop['Ever_Married'] = LabelEncoder().fit_transform(x_train_drop['Ever_Married'])
x_train_drop['Graduated'] = LabelEncoder().fit_transform(x_train_drop['Graduated'])
x_train_drop['Profession'] = LabelEncoder().fit_transform(x_train_drop['Profession'])
x_train_drop['Spending_Score'] = LabelEncoder().fit_transform(x_train_drop['Spending_Score'])


x_test_drop['Gender'] = LabelEncoder().fit_transform(x_test_drop['Gender'])
x_test_drop['Ever_Married'] = LabelEncoder().fit_transform(x_test_drop['Ever_Married'])
x_test_drop['Graduated'] = LabelEncoder().fit_transform(x_test_drop['Graduated'])
x_test_drop['Profession'] = LabelEncoder().fit_transform(x_test_drop['Profession'])
x_test_drop['Spending_Score'] = LabelEncoder().fit_transform(x_test_drop['Spending_Score'])
'''



### 단계2. 훈련셋/검증셋 나누기
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(x_train_drop, y,
                                                  test_size = 0.3,
                                                  random_state=123)

### 단계3. 사용할 모델 정하기 
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 1000,
                               max_features= 5,
                               max_depth = 10,
                               random_state=123)

model.fit(x_train, y_train)

model.score(x_train, y_train)
model.score(x_val, y_val)

train_predict = model.predict(x_train)
train_predict_proba = model.predict_proba(x_train)

val_predict = model.predict(x_val)
val_predict_proba = model.predict_proba(x_val)

from sklearn.metrics import roc_auc_score, f1_score, accuracy_score

print('train_accuracy_score :',  accuracy_score(y_train, train_predict))
print('val_accuracy_score :',  accuracy_score(y_val, val_predict))


### 단계4. best 파라미터 찾기 
from sklearn.model_selection import GridSearchCV
'''
params = {'n_estimators' :[100,200,300, 400],
          'max_depth' : [None, 10,20,30],
          'max_features' : [None, 10, 20,30]}

grid_search = GridSearchCV(estimator=model, param_grid=params, scoring='accuracy')
grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_
'''


### 단계5. test 데이터 예측값 구하기
test_predict = model.predict(x_test_drop)

### 단계6. 예측값 csv 파일 작성 & 제출



















