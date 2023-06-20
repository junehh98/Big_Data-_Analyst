######################################
# Q2.작업형1 : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''    
 문1) 구매가격(price)이 0원인 경우는 제외하고, 구매가격의 평균 보다 큰 
     만족도(survey)의 중앙값을 구하시오.
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\7_제5회_실전문제\data'
a = pd.read_csv(path +'/dataset.csv')  
a.info() # 'data.frame':	217 obs. of  7 variables:

df = a.copy()

target = df[df['price'] != 0]
            
result = target[(target['price']) > (target['price'].mean())]['survey'].median()
print(result)
