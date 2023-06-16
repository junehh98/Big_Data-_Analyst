# -*- coding: utf-8 -*-
'''
 제공되는 데이터는 암진단 관련 데이터이다. 
 
 (가) 제공 데이터 목록 
 
   1. y_train : 환자의 암진단 결과 데이터(학습용)
   2. X_train, X_test : 암에 영향을 미치는 속성(학습용 및 평가용)

 (나) 데이터 형식 및 내용
   1. y_train.csv(569명 데이터)   

         uid  target
   ----------------------         
    0      0       0
    1      1       0
    2      2       0
    3      3       0
    4      4       0
    
    * uid : 환자ID
    * target : 암진단 결과(0: 양성, 1:악성)
    
    2. X_train (569명 데이터), X_test(300 데이터)
     환자 569명에 대한 학습용 데이터(y_train, X_train)를 이용하여
     암진단 예측 모형을 만든 후, 이를 평가용(X_test)에 적용하여 얻은
     300명 환자의 암진단 예측값(악성일 확률)을 다음과 같은 형식의 
     CSV 파일로 생성하시오.
       uid     pred
        0   0.2415
        1   0.9934
        2   0.1250
        3   0.5353
''' 

import pandas as pd

# 데이터 가져오기
path = r'C:\ITWILL\7_BigGisa\2_머신러닝_모델링'

X_train = pd.read_csv(path+'/data/cancer_X_train.csv')
y_train = pd.read_csv(path+'/data/cancer_y_train.csv')
X_test = pd.read_csv(path+'/data/cancer_X_test.csv')


# 훈련셋, 테스트셋 변수 확인 
X_train.info() # 훈련셋 X변수 
y_train.info() # 훈련셋 y변수 
X_test.info() # 테스트셋 X변수(y변수 없음) 

"""
<pandas & sklearn을 활용한 머신러닝 모델링 절차>  
  단계1. 데이터 전처리 & 특징공학 : 결측값,이상치,변수선택/제거,스케일링,인코딩   
  단계2. 훈련셋/검증셋 나누기 : train_test_split, KFold 등
  단계3. 사용할 모델 정하기
     1) RandomForest, XGBoost, LinearRegression 등
     2) 모델학습 : fit(훈련셋 X변수, 훈련셋 y변수)
     3) 모델검증 : 평가지표(roc_auc_score, accuracy_score, MSE, r2_score 등)
  단계4. best 파라미터 찾기 : Grid-search -> 모델학습 -> 모델검증 
  단계5. test 데이터 예측값 구하기 : predict(테스트셋 X변수), predict_proba(테스트셋 X변수)
  단계6. 예측값 csv 파일 작성 & 제출 : 예측값.to_csv('파일명', index = False)
"""
 

### 단계1. 데이터 전처리 & 특징공학  

# 1) DF 합치기 : uid 기준 
df = pd.merge(X_train, y_train, on=['uid']) # df = X + y
df.info()

# 2) 불필요한 칼럼 제거 
new_df = df.drop(['uid'], axis = 1) # 원본 유지 
new_df.shape # (569, 31) : X=30, y=1

# 3) 결측치 처리 : 결측치 적은 경우 제거 
new_df.isnull().sum() # mean smoothness     3
new_df = new_df.dropna(subset=['mean smoothness']) 
new_df.shape # (566, 31)

# 4) 이상치, 스케일링(X), 인코딩(y) : 대상변수 없음 

# [1] X, y변수 분리 
X = new_df.drop(['target'], axis = 1) # y변수 제거 
y = new_df.target
X.shape # (566, 30)
y.shape # (566,)

# [2] 이상치, 스케일링 여부 확인 
des = X.describe() # 요약통계 
des.loc[['mean','std','min','max'], ].T  

# [3] 최소-최대 정규화 : 트리계열 X
from sklearn.preprocessing import MinMaxScaler

X = MinMaxScaler().fit_transform(X = X)
y # 인코딩 되어 있음  


### 단계2. 훈련셋/검증셋 나누기 : [선택]

from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(
    X, y, random_state=123, test_size=0.3)



### 단계3. 사용할 모델 정하기 
from sklearn.ensemble import RandomForestClassifier # 분리트리

# 1) 모델학습 
model = RandomForestClassifier(random_state=123).fit(X=X_train, y=y_train)
'''
훈련셋/검증셋 나누기 생략 시 : full dataset 적용 -> fit(X=X, y=y)
'''
# 2) 모델검증 
dir(model)
print('train score :', model.score(X_train, y_train))
print('val score :', model.score(X_val, y_val))


### 단계4. best 파라미터 찾기 : [선택]
from sklearn.model_selection import GridSearchCV

# 1) 파라미터 선정 : dict
parms = {'n_estimators' : [100, 150, 200],
         'max_depth' : [None, 5, 7],
         'max_features' : ['auto','sqrt']}

# 2) GridSearch model 
gs_model = GridSearchCV(model, param_grid = parms, 
                        scoring='accuracy')

gs_model = gs_model.fit(X=X, y=y) # full dataset 

dir(gs_model)
gs_model.best_params_
# {'max_depth': 7, 'max_features': 'auto', 'n_estimators': 100}

# full dataset
best_model = RandomForestClassifier(random_state=123,
                                    max_depth=7,
                                    max_features='auto',
                                    n_estimators=100).fit(X=X, y=y)


### 단계5. test 데이터 전처리

# 1) id + X 분리 : 각 칼럼 사용 
X_test.info() # 300, 31(uid + X)

uid = X_test.uid # 환자 id 추출 
x = X_test.drop(['uid'], axis = 1) # 소문자 x
x.shape # (300, 30)

# 2) 결측치 없음 : 제거할 경우 관측치 길이 달라짐 
x.isnull().sum() # 결측치 없음 

# 3) 이상치 : 대상변수 없음 

# 4) 스케일링 
des = x.describe()
des.loc[['mean','min', 'max'], ].T

x = MinMaxScaler().fit_transform(X = x)


### 단계6. 예측값 csv 파일 작성 & 제출

# 1) y 예측값
#model.predict(X=x) # class 예측(0 or 1)
y_pred = model.predict_proba(x) # 기본 model : 확률 예측 
y_pred = best_model.predict_proba(x) # best_model 

y_pred.shape # (300, 2) 
y_pred
pred = y_pred[:, 1] # 악성 확률 

# 2) DataFrame 생성 
result = pd.DataFrame({'uid' : uid, 'pred' : pred}, 
                      columns=['uid', 'pred'])
result

# 3) csv 파일 작성 & 제출
result.to_csv(path + '/00001234.csv', index=None)

