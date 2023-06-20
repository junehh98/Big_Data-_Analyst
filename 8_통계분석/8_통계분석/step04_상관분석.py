'''
공분산 vs 상관계수  
1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)를 나타내는 통계     
2. 상관계수 : 공분산을 각각의 표준편차로 나눈어 정규화한 통계
'''

import pandas as pd 
path = r'C:\ITWILL\7_BigGisa\8_통계분석\data'
score_iq = pd.read_csv(path + '/score_iq.csv')
print(score_iq)


# 1. 피어슨 상관계수 행렬 
corr = score_iq.corr(method='pearson')
print(corr)
 
# 2. 공분산 행렬 
cov = score_iq.cov()
print(cov)


# 3. 특정칼럼 기준 
corr['score'] #  점수 기준 상관계수
cov['score'] #  점수 기준 공분산


# 4. 칼럼 : 칼럼 
score_iq['score'].corr(score_iq['iq']) # score와 iq 상관계수 
score_iq['score'].cov(score_iq['iq']) # score와 iq 공분산


