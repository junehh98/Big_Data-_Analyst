######################################
# 제1유형-5 : 데이터 처리 & 통계
######################################

# 유형5 : 통계를 이용한 이상치 처리 
# 제출 : print(result) 

'''
 문) price 칼럼을 대상으로 평균값에서 표준편차의 1.5배 보다 작거나 큰 값을 추출하시오.
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path +'/dataset.csv')  
a.info() # 'data.frame':	217 obs. of  7 variables:



# 1. 통계 구하기 : 평균, 표준편차 
avg = a['price'].mean()
std = a['price'].std()


# 2. outlier step
outlier_step = std * 1.5

min_val = avg - outlier_step # 평균값에서 표준편차의 1.5배 보다 작음
max_val = avg + outlier_step # 평균값에서 표준편차의 1.5배 보다 큼

# 3. 이상치 추출 
df = a[(a['price'] < min_val) | (a['price'] > max_val)]
df.shape  # (31,7)





