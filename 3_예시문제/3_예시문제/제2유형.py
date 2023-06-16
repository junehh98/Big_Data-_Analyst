# -*- coding: utf-8 -*-
"""
 제2유형
 --------------------------------------------------------------------------------------
 아래 백화점 고객의 1년간 구매 데이터이다. 
 
 (가) 제공 데이터 목록 
 
   1. y_train.csv : 고객의 성별 데이터(학습용), csv 형식의 파일 
   2. X_train.csv, X_test.csv : 고객의 상품구매 속성(학습용 및 평가용)
   
 (나) 데이터 형식 및 내용 

   1. y_train.csv(3,500명 데이터)
   
     cust_id   gender
   ----------------------
    0    0       0
    1    1       0
    2    2       1
    3    3       1
    
    * cust_id : 고객ID
    * gender : 고객의 성별(0: 여자, 1:남자)
    
   2. X_train.csv (3,500명 데이터), X_test.csv(2,482 데이터)
   고객 3,500명에 대한 학습용 데이터(y_train.csv, X_train.csv)를 이용하여
   성별예측 모형을 만든 후, 이를 평가용(X_test.csv)에 적용하여 얻은
   2,482명 고객의 성별 예측값(남자일 확률)을 다음과 같은 형식의 CSV 파일로 
   생성하시오.(제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)
  
   custid, gender
    3500, 0.267
    3501, 0.578
    3502, 0.885   
     ...   
     
  (유의사항)
  - 성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리, Feature
    Engineering, 분류 알고리즘 사용, 초매개변수 최적화, 모형 앙상블 등이
    수반되어야 한다.
    
  - 수험번호.csv(예: 0000.csv) 파일이 만들어지도록 코드를 제출한다.
  - 제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점한다.
  - dataset은 'data/y_train.csv'의 형태로 읽어들인다.
"""


# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd

path = r'C:\ITWILL\7_BigGisa\3_예시문제'
X_train = pd.read_csv(path + '/data/X_train.csv', encoding='euc-kr')
X_test = pd.read_csv(path + '/data/X_test.csv', encoding='euc-kr')
y_train =pd.read_csv(path + '/data/y_train.csv', encoding='euc-kr')

# 사용자 코딩

# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)


# --------------------------------------------------------------------------------------


### 단계1. 데이터 전처리 & 특징공학  

# 1) DF 병합(merge) : 공통칼럼 cust_id 기준 
train_full = pd.merge(X_train, y_train, on=['cust_id'])

train_full.shape # (3500, 11)

# 2) 변수 제거 : cust_id
train_full = train_full.drop(['cust_id'], axis = 1)
train_full.info() # X(9) + y(1)

# 3) 결측치 처리 
train_full.isnull().sum()
# 환불금액       2295

# 결측치 비율 50% 이상 : 칼럼 제거 
train_full = train_full.drop(['환불금액'], axis = 1)
train_full.shape # (3500, 9)

# 4) 이상치 처리 : 총구매액, 최대구매액 : 음수 -> 0으로 대체
train_full.loc[train_full['총구매액'] < 0, '총구매액'] = 0
train_full.loc[train_full['최대구매액'] < 0, '최대구매액'] = 0

# 이상치 처리 확인 
train_full['총구매액'].min() # 0
train_full['최대구매액'].min() # 0

# 5) 인코딩 : 문자형 변수 label encoding 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler 

# X,y변수 분리 
X = train_full.drop(['gender'], axis = 1)
y = train_full.gender

# 대상변수 : 주구매상품, 주구매지점
X['주구매상품'] = LabelEncoder().fit_transform(X['주구매상품'])
X['주구매지점'] = LabelEncoder().fit_transform(X['주구매지점'])

# 6) 스케일링 
X = MinMaxScaler().fit_transform(X = X)

   
### 단계2. 데이터 분할 : [선택]
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=234)


### 단계3. 모델 생성   
from sklearn.ensemble import RandomForestClassifier

# 훈련셋 반영 model
model = RandomForestClassifier(random_state=123).fit(x_train, y_train)

# full dataset 반영 model  
model = RandomForestClassifier(random_state=123).fit(X, y)

print('train score :', model.score(x_train, y_train))
print('val score :', model.score(x_val, y_val))


### 단계4. best 파라미터 찾기 : [선택]


### 단계5. Test셋 전처리  
  
# 1) cust_id와 X변수 분리 
cust_id = X_test.cust_id 

x_test = X_test.drop('cust_id', axis=1)
x_test.shape # (2482, 9)

# 2) 결측치 처리 : 환불금액 제거  
x_test.isnull().sum()
# 환불금액       2295

# 훈련셋의  X변수와 동일해야 함  
x_test = x_test.drop(['환불금액'], axis = 1)
x_test.shape # (2482, 8)

# 3) 이상치 처리 : 총구매액, 최대구매액 : 음수 -> 0으로 대체
x_test.loc[x_test['총구매액'] < 0, '총구매액'] = 0
x_test.loc[x_test['최대구매액'] < 0, '최대구매액'] = 0

# 4) 인코딩 : 주구매상품, 주구매지점
x_test['주구매상품'] = LabelEncoder().fit_transform(x_test['주구매상품'])
x_test['주구매지점'] = LabelEncoder().fit_transform(x_test['주구매지점'])


# 5) 스케일링 
x_test = MinMaxScaler().fit_transform(X = x_test)

### 단계6. 예측값 csv 파일 작성 & 제출

# 1) 남자일 확률 예측 
y_pred = final_model.predict_proba(x_test) 
pred = y_pred[:, 1] # 남자일 확률 


# 2) DataFrame 생성 
result = pd.DataFrame({'custid':cust_id, 'gender':pred},
              columns =['custid', 'gender'])


# 3) csv file 작성 & 제출 
result.to_csv(path + '/0000.csv', index=None)










