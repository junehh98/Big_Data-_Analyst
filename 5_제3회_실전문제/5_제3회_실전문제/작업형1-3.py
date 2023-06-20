######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 유형3 : 기본 자료 처리 & 특징 분석
# 제출 : print(result) 

'''
 문3) 각 변수들의 결측치 비율 중 가장 큰 비율값을 가진 변수명은?  
'''

# 데이터 파일 읽기 
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\5_제3회_실전문제\data'
a = pd.read_csv(path +'/stock.csv') 

df = a.copy()
target = df.isnull().sum()
result = target.sort_values(ascending=False).index[0]
print(result)
