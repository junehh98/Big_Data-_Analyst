######################################
### 5. 자료 스케일링 
######################################
"""
 - 자료 스케일링 : 변수 간 서로 다른 척도 일 때 일정한 값의 범위로 조정   
 - 방법 : 정규화와 표준화
  1. 표준화 : X변수를 대상으로 정규분포가 될 수 있도록 평균=0, 표준편차=1로 통일 시킴 
   -> 회귀모델, SVM 계열은 X변수가 정규분포라고 가정하에 학습이 진행되므로 표준화를 적용   
  2. 최소-최대 정규화 : 서로 다른 척도(값의 범위)를 갖는 X변수를 대상으로 최솟값=0, 최댓값=1로 통일 시킴 
   -> 트리모델 계열(회귀모델 계열이 아닌 경우)에서 서로 다른 척도를 갖는 경우 적용
"""
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\1_데이터조작_전처리\data'
a = pd.read_csv(path +'/mtcars.csv') 

df = a.copy() # DF 복제 


# 정규화/표준화 도구 가져오기 
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# 1) 정규화 
X_scaled = MinMaxScaler().fit_transform(X=df)
type(X_scaled) # numpy.ndarray 


# numpy -> pandas 
new_df = pd.DataFrame(X_scaled, columns= [df.columns])
new_df

#요약통계량
print(new_df.describe())


# 2) 표준화 
X_scaled2 = StandardScaler().fit_transform(X=df)
type(X_scaled2) # numpy.ndarray 

# numpy -> pandas 
new_df2 = pd.DataFrame(X_scaled2, columns= [df.columns])
new_df2

#요약통계량
print(new_df2.describe())
