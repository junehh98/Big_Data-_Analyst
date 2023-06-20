######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''    
 문1) 직업유형(job)의 결측치를 빈도수가 가장 많은 값으로 교체한 후  
      직업유형(job)별로 price의 제3사분위수를 모두 더한 값을 출력하시오.
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\6_제4회_실전문제\data'
a = pd.read_csv(path +'/dataset.csv')  
a.info() 

df = a.copy()
df['job'].value_counts() # 3

df.isnull().sum()
df['job'] = df['job'].fillna(3)

target1 = df[df['job']==1]['price'].quantile(0.75)
target2 = df[df['job']==2]['price'].quantile(0.75)
target3 = df[df['job']==3]['price'].quantile(0.75)

result = target1 + target2 + target3
print(result) # 16.1
