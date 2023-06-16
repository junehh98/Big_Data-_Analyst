######################################
### 4. 데이터 인코딩 
######################################

"""
데이터 인코딩 : 머신러닝 모델에서 범주형변수를 대상으로 숫자형의 목록으로 변환해주는 전처리 작업
 - 방법 : 레이블 인코딩(label encoding), 원-핫 인코딩(one-hot encoding)   
 1. 레이블 인코딩(label encoding) : y변수 대상 10진수 인코딩 or 트리모델의 x변수 인코딩
 2. 원-핫 인코딩(one-hot encoding) : 회귀모형, SVM 계열의 x변수 대상 2진수 인코딩 
   -> 회귀모형에서는 인코딩값이 가중치로 적용되므로 원-핫 인코딩(더미변수)으로 변환  
"""


import pandas as pd 

path = r'C:\ITWILL\7_BigGisa\1_데이터조작_전처리\data'
a = pd.read_csv(path +'/skin.csv') 
a.info()
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   cust_no      30 non-null     int64  -> 변수 제외 
 1   gender       30 non-null     object -> x변수 
 2   age          30 non-null     int64 
 3   job          30 non-null     object
 4   marry        30 non-null     object
 5   car          30 non-null     object
 6   cupon_react  30 non-null     object -> y변수(쿠폰 반응) 
''' 

## 변수 제거 : cust_no
df = a.drop('cust_no', axis = 1)
df.info()


### 1. 레이블 인코딩 : y변수 또는 트리모델 계열의 x변수 인코딩  
from sklearn.preprocessing import LabelEncoder # 인코딩 도구 

# 1) 쿠폰 반응 범주 확인 
df.cupon_react.unique() # array(['NO', 'YES'], dtype=object) 

# 2) 인코딩 & 칼럼 추가 
df['label'] = LabelEncoder().fit_transform(df['cupon_react']) # y변수  

# 반환값 
print(df['label']) 



### 2. 원-핫 인코딩 : 회귀모델 계열의 x변수 인코딩  

# 1) n개 목록으로 가변수(더미변수) 만들기 
one_hot = pd.get_dummies(data=df) # object형 변수 대상  
one_hot 


# 2) n개 목록으로 가변수(더미변수) 만들기 : 특정 변수 지정   
one_hot2 = pd.get_dummies(data=df, 
                          columns=['label','gender','job','marry'])
one_hot2.info() # Data columns (total 12 columns):

    
# 3) n-1개 목록으로 가변수(더미변수) 만들기   
one_hot3 = pd.get_dummies(data=df, drop_first=True) 
one_hot3 


# 4) 한 개 변수로 가변수 만들기  
gender_dummy = pd.get_dummies(data=df['gender']) # drop_first=False
df_new = pd.concat([df, gender_dummy], axis = 1)



