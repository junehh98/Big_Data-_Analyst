######################################
# Q2.작업형1 : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''
  문3) 도내.외 순전출학생(전출-전입)이 가장 많은 자치구의 top3의 전체 학생수는?

<자료 참고> 서울열린데이터광장 
2023년 서울시 학생변동상황에 대한 통계자료로 초등학교의 시내·시외 전입 및 전출에 의한 학생이동수 제공
'''
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\7_제5회_실전문제\data'
a = pd.read_csv(path +'/학생변동상황(전출·전입)_202306.csv', thousands=',') 
a.info()
'''
 0   자치구별     26 non-null     int64
 1   초_도내_전출  26 non-null     int64
 2   초_도외_전출  26 non-null     int64
 3   초_도내_전입  26 non-null     int64
 4   초_도외_전입  26 non-null     int64
'''
df = a.copy()
df['순전출'] = (df['초_도내_전출'] + df['초_도외_전출']) - (df['초_도내_전입'] + df['초_도외_전입'])
df['순전출'].sort_values(ascending=False).head(4)

result = 1398+1395+1316
print(result)


