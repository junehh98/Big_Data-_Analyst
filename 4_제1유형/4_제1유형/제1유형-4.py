######################################
# 제1유형-4 : 데이터 처리 & 통계
######################################

# 유형4 : 자료형 변환과 이상치 처리 
# 제출 : print(result) 

'''
 문) cost 칼럼을 대상으로 IQR 방식으로 이상치를 처리하시오.
    <조건1> cost 칼럼의 자료형을 실수형으로 변환 
    <조건2> 정상범주의 레코드 추출 
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path +'/descriptive.csv')  
a.info() # 'data.frame':	300 obs. of  8 variables:


# 1. 실수형 변환 
df = a.copy()
cost = df['cost']
cost.dtype # dtype('O') : Object

# Object -> float32
cost = cost.astype('float32')
# ValueError: could not convert string to float: ''
# 특수문자 또는 공백은 숫자형 변환 안됨 

cost.unique() # 유일값 확인 

# 특수문자 또는 공백 -> 0으로 대체  
df['cost'] = cost.replace('               ', 0) 
df['cost'] = df['cost'].astype('float32') # 실수형 변환 
df.info()


# 2. IQR 구하기 
des = df['cost'].describe()

q1 = des['25%']
q3 = des['75%']

iqr = q3 - q1 
iqr 

outlier_step = iqr * 1.5
min_val = q1 - outlier_step
max_val = q3 + outlier_step
# 0.7000002861022949 ~ 9.499999523162842

# 3. 정상범주 레코드 추출  
new_df = df[(df['cost'] >= min_val) & (df['cost'] <= max_val)]  
new_df.shape  # (251, 8)   







