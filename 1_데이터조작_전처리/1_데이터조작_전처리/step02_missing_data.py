######################################
### 2. 결측치 처리
######################################

'''
x변수 결측치 확인, 제거, 다른값 대체
'''

import pandas as pd
path = r'C:\ITWILL\7_BigGisa\1_데이터조작_전처리\data'
a = pd.read_csv(path +'/mtcars.csv') 
a.info()


# 1. 결측치(NaN) 확인  
a.isnull().any() 
a.isnull().sum()  


# 2. 전체 칼럼 기준 결측치 제거 
new_df = a.dropna()
new_df.shape # (29, 11)
new_df.isnull().sum() # 없음 


# 3. 특정 칼럼 기준 결측치 제거 -> subset 생성  
new_df2 = a.dropna(subset =['disp']) # default : 행축 기준
new_df2.shape # (30, 11)
new_df2.isnull().sum() # disp 없음 


# 4. 전체 결측치 다른값 대체 
new_df3 = a.fillna(0) 
new_df3.shape # (32, 11)
new_df3.isnull().sum() # 없음


# 5. 특정 칼럼 결측치 다른값 대체 
new_df4 = a.copy()
new_df4['disp'].mean() 
new_df4['disp'].fillna(new_df4['disp'].mean(), inplace=True)

