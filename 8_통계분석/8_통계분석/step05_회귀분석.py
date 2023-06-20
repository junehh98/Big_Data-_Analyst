# -*- coding: utf-8 -*-
"""
scipy 패키지 이용 
 1. 단순선형회귀분석 
 2. 다중선형회귀분석 
"""

from scipy import stats
import pandas as pd

path=r'C:\ITWILL\7_BigGisa\8_통계분석\data'
score_iq = pd.read_csv(path + '/score_iq.csv')
score_iq.info()

# 1. 단순선형회귀분석 
'''
x -> y
'''

# 1) 변수 생성 
x = score_iq['iq'] # 독립변수 
y = score_iq['score'] # 종속변수 

# 2) model 생성 
model = stats.linregress(x, y)
print(model)
'''
LinregressResult(
    slope=0.6514309527270075, : x 기울기 
    intercept=-2.8564471221974657, : y 절편 
    rvalue=0.8822203446134699, : 설명력
    pvalue=2.8476895206683644e-50, : F검정 : 유의성검정 
    stderr=0.028577934409305443) : 표준오차 
'''



# 2. 다중선형회귀분석 : formula 형식 
from statsmodels.formula.api import ols


# 상관계수 행렬 
corr = score_iq.corr()

print(corr['score'])


obj = ols(formula='score ~ iq + academy + tv', data = score_iq)

model = obj.fit()

# 회귀계수값 반환 
print('회귀 계수값\n%s'%(model.params))
print('Pvalue :', model.pvalues)
print('Rsquaured : ', model.rsquared)


# 회귀분석 결과 제공  
print(model.summary()) 




