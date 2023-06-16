######################################
# Q1.제1유형(10점) : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''
 문2) 데이터셋에서 2018년도 자료를 대상으로 전체 국가의 출생아수의 평균 보다 큰 국가 개수는?
      <조건> 결측치(NA)는 0으로 대체 
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\5_제3회_실전문제\data'
a = pd.read_csv(path +'/births_num.csv', encoding='euc-kr') 




