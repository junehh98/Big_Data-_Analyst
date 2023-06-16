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
X_test = pd.read_csv(path +'/X_test.csv', encoding='euc-kr')  # 평가용 X변수
X_train = pd.read_csv(path + '/X_train.csv', encoding='euc-kr') # 훈련용 X변수 
y_train = pd.read_csv(path + '/y_train.csv', encoding='euc-kr') # 훈련용 y변수 



### 단계1. 데이터 전처리 & 특징공학 

# 1) DF 병합 : 원본 자료 보관   
df = pd.merge(X_train, y_train, on='Date') # 공통칼럼(o)

# 2) 칼럼 제거 
df = df.drop(['Date'], axis = 1)
df.shape # (256, 12)

# 3) 결측치 처리
df.isnull().sum() #  결측치 변수 : Sunshine, WindGustSpeed

# 결측치 제거 
df = df.dropna()


# 4) 인코딩 : label encoding 
from sklearn.preprocessing import LabelEncoder

df.info() # object형 변수 확인 
df['WindGustDir'] = LabelEncoder().fit_transform(df['WindGustDir'])


# 5) 스케일링 : 트리계열  
from sklearn.preprocessing import MinMaxScaler 

# 1) X, y변수 분리 
y = df.rain  
X = df.drop('rain', axis = 1)

X = MinMaxScaler().fit_transform(X)

# 스케일링 확인 
X.min()
X.max()


### 단계2. 훈련셋/검증셋 나누기 
from sklearn.model_selection import train_test_split    

x_train, x_val, y_train, y_val = train_test_split(
    X, y, random_state=123)


### 단계3. 사용할 모델 정하기 
from sklearn.ensemble import RandomForestClassifier 

# 1) model 학습 : 성능 비교 & model 선정  
rf_model = RandomForestClassifier(random_state=123).fit(x_train, y_train)

# 2) model 평가 : 예측력 높은 model 선택 
rf_model.score(x_train, y_train) 
rf_model.score(x_val, y_val) 

# 3) 전체 훈련셋으로 model 학습 
final_model = RandomForestClassifier(random_state=123).fit(X, y)


### 단계4. best 파라미터 찾기 : [생략]


### 단계5. test 데이터 예측값 구하기
X_test.info() # 평가셋 확인 

# 1) date와 X 분리 
date = X_test['Date'] # Date 칼럼 보관
x_test = X_test.drop(['Date'], axis = 1) 

# 2) 결측치 처리
x_test.isnull().sum() #  Sunshine, WindGustSpeed

x_test['Sunshine'] = x_test['Sunshine'].fillna(0)
x_test['WindGustSpeed'] = x_test['WindGustSpeed'].fillna(0)

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
result = pd.DataFrame({'Date' : date, 'rain' : rain})

# 4) file save 
result.to_csv(path + '/0001234.csv', index = False)



