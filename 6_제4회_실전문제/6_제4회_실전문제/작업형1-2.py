######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''
 문2) 선행주가수익율(Forward P/E)과 주가수익성장율(PEG)을 예상주가수익율로 정의하고, 
    주가수익율(P/E)에서 예상주가수익율이 차지하는 비율을 계산, 그 비율이  0.7보다 작고
    0.5보다 크며, 국적(Country)이 USA인 건수를 정수로 출력하시오.

    <선행 조건> 결측치를 갖는 모든 행은 제거한다.
'''
# 1. 예상주가수익율 = 선행주가수익유 + 주가수익성장율

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\6_제4회_실전문제\data'
a = pd.read_csv(path +'/stock_data.csv') 
'''
<주요 변수 설명> 
Market Cap : 시가총액
P/S : 주가매출비율 
P/B : 주가순자산비율 
'''


df = a.copy()
df = df.dropna()
df['예상주가수익율'] = df['Forward P/E'] + df['PEG']
df['target'] = df['예상주가수익율']/df['P/E']
df1 = df[(df['target'] > 0.5) & (df['target'] < 0.7)]
df2 = df1[df1['Country'] == 'USA']
result = len(df2)
result = int(result)
print(result) # 57
