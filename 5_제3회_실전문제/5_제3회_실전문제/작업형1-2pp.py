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

#a.info()
a.head()

a.shape # (5, 106)
'''
2018 : 3행 
전체 국가 : 2열~106열 
'''

# 1. 2018년도 전체 국가 자료 추출 
'''
DF.iloc[행_숫자, 열_숫자]
DF.loc[행_명칭, 열_명칭]
'''

year2018 = a.iloc[2, 1:] # 3행, year 칼럼 제외 전체
year2018.shape # (105,)

# 2. 결측치 0으로 대체 
year2018.isnull().sum() # 27

year2018 = year2018.fillna(0)
year2018.isnull().sum() # 0


# 3. 출생아 평균 
# 자료형 확인 & 형 변환 
year2018.dtype # dtype('O') : Object
year2018 = year2018.astype('float32')
avg = year2018.mean()
avg # 191630.375

# 4. 평균 이상 국가 수 
result = year2018[year2018 >= avg].shape  # (21,)
print(result[0]) # 21











