'''
t검정 : t 분포에 대한 가설검정  
  1. 한 집단 평균 검정  
  2. 두 집단 평균 검정
  3. 대응 두 집단
'''

from scipy import stats # test
import numpy as np # sampling


# 1. 한 집단 평균 검정 : 남자 평균 키(모평균)  
sample_data = np.random.uniform(172, 179, size=29) # 키 표본추출 
print(sample_data)

# 기술통계  
print('평균 키 =', sample_data.mean()) 

# 단일집단 평균차이 검정 
one_test = stats.ttest_1samp(sample_data, 176, 
                             alternative="two-sided") 
print('t검정 통계량 = %.3f, pvalue = %.5f'%(one_test))


# 2. 두 집단 평균 검정 : 남여 평균 점수 차이 검정 
female_score = np.random.uniform(50, 100, size=30) # 여학생 점수  
male_score = np.random.uniform(45, 95, size=30) # 남학생 점수  

two_sample = stats.ttest_ind(female_score, male_score, 
                             alternative="two-sided")
print(two_sample)
print('두 집단 평균 차이 검정 = %.6f, pvalue = %.6f'%(two_sample))



# 3. 대응 두 집단 : 복용전 65 -> 복용후 60 몸무게 변환  
'''
µd : (복용전 몸무게 - 복용후 몸무게)의 평균 
H0 : Ud = 0
H1 : Ud < 0 
'''

before = np.random.randint(60, 65, size=30)  # 복용전 몸무게 
after = np.random.randint(59, 64,  size=30)  # 복용후 몸무게 

paired_sample = stats.ttest_rel(before, after, alternative='less')
print(paired_sample)
print('t검정 통계량 = %.5f, pvalue = %.5f'%paired_sample)
# t검정 통계량 = 1.79505, pvalue = 0.95846




