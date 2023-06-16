'''
3. 이상치 처리 
 - IQR 방식으로 mpg 칼럼의 이상치 처리하기
 - 결측치는 평균으로 대체  
'''

import pandas as pd
path = r'C:\ITWILL\7_BigGisa\1_데이터조작_전처리\data'
a = pd.read_csv(path +'/mtcars.csv') 
a.info() # total 11 columns

df = a.copy() # df 복제 
df.shape # (32, 11)


# 1. 결측치 확인 & 처리  
df.isnull().sum() # mpg     1

# 결측치 처리 
df['mpg'] = df['mpg'].fillna(df['mpg'].mean())


'''
IQR(Inter Quartile Range)방식 이상치 처리
 IQR = Q3 - Q1 : 제3사분위수 - 제1사분위수
 outlier_step = 1.5 * IQR
 정상범위 : Q1 - outlier_step ~ Q3 + outlier_step
'''

# 2. 사분위수 구하기 
des = df.describe()
q1 = des.loc['25%', 'mpg']   # 제1사분위수 : 전체 칼럼 
q3 =  des.loc['75%', 'mpg']  # 제3사분위수 : 전체 칼럼 


# 3. outlier_step 
iqr = q3 - q1
print(iqr)

# outlier_step 
outlier_step = 1.5 * iqr
outlier_step

# 4. min_val, max_val 만들기
min_val = q1 - outlier_step 
max_val = q3 + outlier_step 


# 5. 이상치 찾기 : 1개 발견 
new_df = df[(df['mpg'] < min_val) | (df['mpg'] > max_val)]
new_df.shape # (1, 11)
                         

# 6. 정상범위 : 이상치 제거 
new_df2 = df[(df['mpg'] >= min_val) & (df['mpg'] <= max_val)]
new_df2.shape # (31, 11)

