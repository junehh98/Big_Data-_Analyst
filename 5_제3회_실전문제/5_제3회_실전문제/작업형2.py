# -*- coding: utf-8 -*-
"""
################################################
# Q2. 작업형2(40점) : 데이터 모형 구축 & 평가 
################################################

 아래 날씨 관련 데이터는 2년 간 기록한 데이터이다.
  [참고] 기출문제에 유형에 맞게 변형된 자료

 (가) 제공 데이터 목록 
   y_train.csv : 날짜와 비유 유무 데이터(학습용), csv 형식 파일 
   X_train.csv : 날짜와 날씨에 영향을 미치는 변수(학습용), csv 형식 파일 
   X_test.csv : 날짜와 날씨에 영향을 미치는 변수(평가용), csv 형식 파일 

 (나) 데이터 형식과 내용 
    y_train.csv
    
             Date  rain
    -------------------
    1   2015-08-13    0
    2   2015-10-01    0
    3   2015-08-28    0
        생략
    8   2015-10-12    0
    9   2015-01-02    0
    10  2015-10-05    1

  X_train.csv(256), X_test.csv(110)
  
    Date MinTemp MaxTemp Rainfall Sunshine WindGustDir WindGustSpeed WindSpeed ...
    -----------------------------------------------------------------------------------
    1  2015-08-13     0.1    10.4      0.0      7.9          SW            59    
    2  2015-10-01     2.3    16.8      0.0     11.4          NW            41      
    3  2015-08-28    -3.3    15.1      0.0       NA          SW            30      
       생략 
    8  2015-10-12     8.2    22.4      0.0     11.2          NW            31      
    9  2015-01-02    14.3    35.0      0.0     10.5          ES            41      
    10 2015-10-05    14.4    20.7      7.6      4.9          NW            33      

 (다) 예측모델 & csv 파일 저장 
    학습데이터(y_train.csv, X_train.csv)를 이용하여 비가올 예측모델을 만든 후  
    이를 평가용 데이터(X_test.csv)에 적용하여 비 유무 예측값(비가 올 확률)을 
    다음과 같은 형식의 csv 파일로 생성하시오.(모델의 성능은 ROC-AUC 평가지표에 따라 채점) 
              date   yes
    1   2014-11-05 0.110
    2   2014-11-11 0.538
    3   2014-11-22 0.012
    4   2014-11-24 0.875
         :

 (유의사항)
  성능이 우수한 예측모델을 구하기 위해서 적절한 데이터 전처리, 
  Feature Engineering(결측치 처리, 이상치 처리, 변수변환, 스케일링, 차원축소), 
  분류알고리즘 선택, 모형 알상블 등이 수반되어야 한다.
  
 제출 : result.to_csv('수험번호.csv', index = False)
"""

# (라) 데이터 파일 읽기 
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\5_제3회_실전문제\data'
x_test = pd.read_csv(path +'/X_test.csv', encoding='euc-kr')  # 평가용 X변수
x_train = pd.read_csv(path + '/X_train.csv', encoding='euc-kr') # 훈련용 X변수 
y_train = pd.read_csv(path + '/y_train.csv', encoding='euc-kr') # 훈련용 y변수 



### 단계1. 데이터 전처리 & 특징공학 
x_test_drop = x_test.drop(columns = 'Date')
x_train_drop = x_train.drop(columns = 'Date')

x_train_drop.isnull().sum()
x_test_drop.isnull().sum()

# train변수 결측치 처리
x_train_drop['Sunshine'] = x_train_drop['Sunshine'].fillna(x_train_drop['Sunshine'].mean())
x_train_drop['WindGustSpeed'] = x_train_drop['WindGustSpeed'].fillna(x_train_drop['WindGustSpeed'].mean())


# test변수 결측치 처리
x_test_drop['Sunshine'] = x_test_drop['Sunshine'].fillna(x_test_drop['Sunshine'].mean())
x_test_drop['WindGustSpeed'] = x_test_drop['WindGustSpeed'].fillna(x_test_drop['WindGustSpeed'].mean())



# 4) 인코딩 : label encoding 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler



x_train_drop.info() # object형 변수 확인 
x_train_drop['WindGustDir'] = LabelEncoder().fit_transform(x_train_drop['WindGustDir'])
x_test_drop['WindGustDir'] = LabelEncoder().fit_transform(x_test_drop['WindGustDir'])




x_test_drop = x_test_drop[x_train_drop.columns]

y = y_train['rain']

# 5) 스케일링 : 트리계열  
'''
from sklearn.preprocessing import MinMaxScaler 

# 1) X, y변수 분리 
y = df.rain  
X = df.drop('rain', axis = 1)

X = MinMaxScaler().fit_transform(X)

# 스케일링 확인 
X.min()
X.max()
'''

### 단계2. 훈련셋/검증셋 나누기 
from sklearn.model_selection import train_test_split    

x_train, x_val, y_train, y_val = train_test_split(
    x_train_drop, y, random_state=123)


### 단계3. 사용할 모델 정하기 
from sklearn.ensemble import RandomForestClassifier 

# 1) model 학습 : 성능 비교 & model 선정  
model = RandomForestClassifier(n_estimators = 1000,
                               max_features = 50,
                               max_depth = 5,
                               random_state=123)

# 2) model 평가 : 예측력 높은 model 선택 



# 3) 전체 훈련셋으로 model 학습 
model.fit(x_train, y_train)

model.score(x_train, y_train) 
model.score(x_val, y_val) 

train_predict = model.predict(x_train)
train_predict_proba = model.predict_proba(x_train)[:,1]

val_predict = model.predict(x_val)
val_predict_proba = model.predict_proba(x_val)[:,1]


from sklearn.metrics import roc_auc_score

print('train_roc_auc_score :', roc_auc_score(y_train, train_predict_proba))
print('val_roc_auc_score :', roc_auc_score(y_val, val_predict_proba))

test_predict = model.predict(x_test_drop)
test_predict_proba = model.predict_proba(x_test_drop)[:,1]

result = pd.DataFrame({'Date' : x_test.Date, 'rain' : test_predict_proba})

### 단계4. best 파라미터 찾기 : [생략]


### 단계5. test 데이터 예측값 구하기
#X_test.info() # 평가셋 확인 

# 1) date와 X 분리 
#date = X_test['Date'] # Date 칼럼 보관
#x_test = X_test.drop(['Date'], axis = 1) 

# 2) 결측치 처리
#x_test.isnull().sum() #  Sunshine, WindGustSpeed

#x_test['Sunshine'] = x_test['Sunshine'].fillna(0)
#x_test['WindGustSpeed'] = x_test['WindGustSpeed'].fillna(0)

# 3) 인코딩 
x_test['WindGustDir'] = LabelEncoder().fit_transform(x_test['WindGustDir'])

# 4) 스케일링 
x_test = MinMaxScaler().fit_transform(x_test) 


### 단계6. 예측값 csv 파일 작성 & 제출

# 1) 테스트 셋 반영 
pred = final_model.predict_proba(x_test) # 확률 예측 

# 2) 비올 확률 
rain = pred[:, 1]

# 3) df 생성 
result = pd.DataFrame({'Date' : Date, 'rain' : rain})

# 4) file save 
result.to_csv(path + '/0001234.csv', index = False)



