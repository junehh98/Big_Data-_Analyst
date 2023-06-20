# -*- coding: utf-8 -*-
"""
step01_distribution_test.py

확률분포와 검정(test)

1. 정규성 검정 : 연속확률분포 
2. 이항검정 : 이산확률분포  
"""

from scipy import stats # 확률분포 + 검정
import matplotlib.pyplot as plt # 확률분포의 시각화 


dir(stats) # 검정관련 함수 
'''
binom_test() : 이항검정
chi2_contingency() # 변수2개 - 이원카이제곱 
chisquare() # 변수1개 - 일원카이제곱
ttest_1samp() # 단일표본
ttest_ind() # 독립표본 
ttest_rel() # 대응표본
shapiro() # 정규성검정 
'''


### 1. 정규분포의 검정(정규성 검정)

# 1) 정규분포 객체 생성 
mu, sigma = 0, 1
norm_obj = stats.norm(mu, sigma)

# 2) 확률변수 X : 시행횟수 N번으로 확률변수 X 만들기  
N = 1000 # sample 수 
X = norm_obj.rvs(size = N) # N번 시뮬레이션 

plt.hist(X)
plt.show()


# 3) 정규성 검정 
# 귀무가설(H0) : 정규분포와 차이가 없다.
print(stats.shapiro(X))

statistic, pvalue = stats.shapiro(X)
print('검정통계량 = ', statistic)
print('p-value = ', pvalue)




### 2. 이항검정 : 이항분포를 이용한 가설검정 
'''
 - 이항분포 : 2가지 범주(성공 or 실패)를 갖는 이산확률분포
 - 이항분포 : 베르누이분포, 이항분포
 - 베르누이 분포 : B(N=1, P) -> 독립시행(확률실험) 1회 
 - 이항분포 : B(N=n, P) -> 베르누이 시행횟수 n번 
''' 



'''
1. 연구환경 
  150명의 합격자 중에서 남자 합격자가 62명일 때 95% 신뢰수준에서 
  남여 합격률에 차이가 있다고 할수 있는가?

2. H0 : 남여 합격율(p)은 차이가 없다.(P=0.5) 
'''

#help(stats.binom_test)
'''
binom_test(x, n=None, p=0.5, alternative='two-sided')
 x : 성공횟수, n : 시행회수, p : 귀무가설 확률(0.5), alternative='two-sided' : 양측검정 
''' 

x = 62 # 성공회수 
pvalue = stats.binom_test(x=x, n=150, p=0.5, alternative='two-sided') # 성공횟수, 시행횟수 
print('n = %d, pvalue= %.7f'%(x, pvalue)) 
# n = 62, pvalue= 0.0408685


alpha = 0.05 

if pvalue > 0.05 : # 유의확률 > 유의수준 
    print(f"p-value({pvalue}) >= 0.05 : 남여 합격률에 차이가 없다.")
else:
    print(f"p-value({pvalue}) < 0.05 : 남여 합격률에 차이가 있다.")
    
'''    
p-value(0.040868493866493945) < 0.05 : 남여 합격률에 차이가 있다.

[해설] 시행횟수=150, 성공횟수=62 일때 유의확률 : 4.087%       
 따라서 유의확률이 유의수준 0.05보다 작기 때문에 남여 합격률에 차이가 있다.
''' 

