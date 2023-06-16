######################################
# Q2.제1유형-1 : 데이터 처리 & 통계
######################################
# 필요한 패키지 : pandas, numpy, sklearn  

# 유형1 : 특정 자료 추출(특정 행 또는 특정 열) 후 통계 구하기 
# 제출 : print(result) 

'''
문) wt 칼럼을 내림차순 정렬 후 상위 10개를 대상으로 표준편차를 구하시오. 
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path +'/mtcars.csv')  

#a.info()

wt = a.wt
wt
#dir(wt) # sort_values
#help(wt.sort_values) # 함수 사용법 

wt_sorted = wt.sort_values(ascending=False)
wt_sorted

top10 = wt_sorted.head(10)

#dir(top10)
std = top10.std()

print(std) # 0.796570489313058

# 소수점 3자리 반올림
import numpy as np 
print(np.round(std, 3)) # 0.797












