######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''
  문3) 7월~8월 사이의 자료에서 평균 이상의 강우(Rainfall)를 추출하고,  
         빈도수가 가장 많은 돌풍 방향(WindGustDir)을 출력하시오. 
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\6_제4회_실전문제\data'
a = pd.read_csv(path +'/weather.csv', encoding='euc-kr') 
a.info()

df = a.copy()
df['Date'] = pd.to_datetime(df['Date'])

target = df[(df['Date'].dt.month == 7) | (df['Date'].dt.month == 8)][['Rainfall', 'WindGustDir']]
target2 = target[target['Rainfall'] >= target['Rainfall'].mean()]
result = target2['WindGustDir'].value_counts().index[0]
print(result)
