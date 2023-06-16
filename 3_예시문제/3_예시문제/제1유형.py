# -*- coding: utf-8 -*-
"""
 작업형 1
 --------------------------------------------------------------------------------------
 mtcars 데이터셋(data/mtcars.csv)의 qsec 칼럼을 최소최대척도(min-max scale)로 
 변환 후 0.5보다 큰 값을 가지는 레코드 수를 구하시오.
"""

# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\3_예시문제'
a = pd.read_csv(path + '/data/mtcars.csv', index_col=0)

# 사용자 코딩

# 답안 제출 예시
# print(평균변수값)

# --------------------------------------------------------------------------------------
# 1. qsec 칼럼 추출 
qsec = a.qsec # a.['qsec']
  
# 2. 최소최대척도 스케일링 
from sklearn.preprocessing import MinMaxScaler # 0~1 사이 정규화

qsec_scaled = MinMaxScaler().fit_transform(qsec.to_frame()) # 2d 형태

# DataFrame에 칼럼 추가 & 요약통계량 
a['qsec_2d'] = MinMaxScaler().fit_transform(qsec_2d)
a['qsec_2d'].describe()


# 3. 0.5보다 큰 값 추출
result = a[a['qsec_2d'] > 0.5] 

# 결과 출력 
print(result.shape[0]) # 9
