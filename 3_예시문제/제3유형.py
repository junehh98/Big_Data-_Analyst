'''
 제3유형
 --------------------------------------------------------------------------------------
주어진 데이터에는 고혈압 환자 120명의 치료 전후의 혈압이 저장되어 있다.
해당 치료가 효과가 있는지(즉 치료 후의 혈압이 감소했는지) 쌍체 표본 t-검정
(paired t-test)를 통해 답하고자 한다.
가설은 아래와 같다.

µd : (치료 후 혈압 - 치료전 혈압)의 평균 
               H0 : µd >= 0
               H1 : µd < 0  : 방향성을 갖는 대립가설 

- bp_before : 치료 전 혈압
- bp_after : 치료 후 혈압

1) µd의 표본평균을 입력하시오.(반올림하여 소수 둘째자리까지 계산)
2) 위의 가설을 검정하기 위한 검정통계량을 입력하시오.(반올림하여 소수 넷째자리까지 계산)
3) 위의 통계량에 대한 p-값을 구하여 입력하시오.(반올림하여 소수 넷째자리까지 계산)
4) 유의수준 0.05 하에서 가설검정의 결과를 (채택/기각) 중 하나를 선택하여 입력하시오.
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\3_예시문제'
a = pd.read_csv(path +'/data/blood_pressure.csv', index_col=0)

a.info()

bp_before = a.bp_before # 치료 전 
bp_after = a.bp_after # 치료 후 

ud = bp_after - bp_before

ud.mean() # -5.091666666666667

import numpy as np 
np.round(ud.mean(), 2) # 1) µd의 표본평균 = -5.09

from scipy import stats # 가설검정 

dir(stats)
'''
ttest_1samp : 단일표본 
ttest_ind : 독립표본 
ttest_rel : 대응표본 
'''
result = stats.ttest_rel(bp_before, bp_after) # 방향성 없음(순서무관) 
result 
'''
(statistic=3.3371870510833657, 
 pvalue=0.0011297914644840823)
'''
result = stats.ttest_rel(bp_before,bp_after, 
                         alternative='less') # 방향성 있음(후, 전) 
result
'''
Ttest_relResult(statistic=3.3371870510833657, 
                pvalue=0.0005648957322420411)
'''

result = stats.ttest_rel(bp_before, bp_after,  
                         alternative='greater') # 방향성 있음(후, 전) 
result
'''
Ttest_relResult(statistic=3.3371870510833657, 
                pvalue=0.0005648957322420411)
'''

print(np.round(result[0],4)) # 2) 3.3372
print(np.round(result[1],4)) # 3) 0.0011

ttest_result = '채택' if result[1] > 0.05 else '기각'
print(ttest_result) # 4) 기각

'''
전과 후 차이가 있는 경우 : 양측검정 (사전,사후,alternative='two-sided')
후-전 평균이 음수 경우 : 단측검정 (사전,사후, alternative='less')
후-전 평균이 음수 경우 : 단측검정 (사전,사후, alternative='greater')
'''

'''
귀무가설 : A=B
대립가설 : A≠B (우리의 주장)
t.test(sample_A,sample_B, paired=TRUE)

귀무가설 : A=B
대립가설 : A<B (우리의 주장)
t.test(sample_A,sample_B, paired=TRUE, alternative="less")

귀무가설 : A=B
대립가설 : A>B (우리의 주장)
t.test(sample_A,sample_B, paired=TRUE, alternative="greater")
'''












