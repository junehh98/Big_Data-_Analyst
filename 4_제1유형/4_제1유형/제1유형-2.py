######################################
# 제1유형-2 : 데이터 처리 & 통계
######################################

# 유형2 : 칼럼 이용 조건색인 & 특징 분석
# 제출 : print(result) 

'''
문) 20대와 30대 고객의 age와 price의 상관계수를 각각 구하고, 두 값을 합하시오.
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path +'/dataset.csv')  
a.info() # 'data.frame':	217 obs. of  7 variables:
'''
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   resident  217 non-null    int64  
 1   gender    217 non-null    int64  
 2   job       205 non-null    float64
 3   age       217 non-null    int64  
 4   position  208 non-null    float64
 5   price     217 non-null    float64
 6   survey    217 non-null    int64 
'''

age = a.age 
age.describe()
'''
mean      44.170507
min       20.000000
max       69.000000
'''

# 1) 20대 : 20~29
age20 = a[(a.age >=20) & (a.age <=29)]
age20.shape  # (49, 7)

# 2) 20대 상관계수 
age20_cor = age20.corr()
cor1 = age20_cor.loc['price','age']
cor1 #  0.38160568150333113

# 3) 30대 : 30~39
age30 = a[(a.age >=30) & (a.age <=39)]
age30.shape  # (30, 7)

# 4) 30대 상관계수 
age30_cor = age30.corr()
cor2 = age30_cor.loc['price','age']
cor2 # -0.19833985987374733

# 5) 결과변수 
result = cor1 + cor2
print(result) # 0.1832658216295838




  









