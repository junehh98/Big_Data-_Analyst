'''
 카이제곱 검정(chisquare test) 
  - 확률변수의 적합성 검정 - 일원  
  - 두 집단변수 간의 독립성 검정 - 이원 
  - 검정통계량(기대비율) = sum( (관측값 - 기댓값)**2 / 기댓값 )
'''

from scipy import stats # 확률분포 검정 


# 1. 일원 chi-square(1개 변수 이용) : 적합성 검정 
'''
 귀무가설 : 관측치와 기대치는 차이가 없다.
 대립가설 : 관측치와 기대치는 차이가 있다. 
'''

# 주사위 적합성 검정 
real_data = [4, 6, 17, 16, 8, 9] # 관측값 - 관측도수 
exp_data = [10,10,10,10,10,10] # 기대값 - 기대도수 
chis = stats.chisquare(real_data, exp_data)
print(chis)
print('statistic = %.3f, pvalue = %.3f'%(chis)) 



# 2. 이원 chi-square(2개 변수 이용) : 교차행렬의 관측값과 기대값으로 검정
'''
 귀무가설 : 교육수준과 흡연율 간에 관련성이 없다.(기각)
 대립가설 : 교육수준과 흡연율 간에 관련성이 있다.(채택)
'''

# 파일 가져오기
import pandas as pd

path = r'C:\ITWILL\7_BigGisa\8_통계분석\data'
smoke = pd.read_csv(path + "/smoke.csv")
smoke.info()

# <단계 1> 변수 선택 
education = smoke.education # smoke['education']
smoking = smoke.smoking # smoke['smoking']


# <단계 2> 교차분할표 
tab = pd.crosstab(index=education, columns=smoking)
print(tab) # 관측값 


# <단계3> 카이제곱 검정 : 교차분할표 이용 
chi2, pvalue, df, evalue = stats.chi2_contingency(observed= tab)  

# chi2 검정통계량, 유의확률, 자유도, 기대값  
print('chi2 = %.6f, pvalue = %.6f, d.f = %d'%(chi2, pvalue, df))
# chi2 = 18.910916, pvalue = 0.000818, d.f = 4

