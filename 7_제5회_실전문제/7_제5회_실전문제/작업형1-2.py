######################################
# Q2.작업형1 : 데이터 처리 & 통계
######################################

# 제출 : print(result) 

'''
문2) 제공되는 자료의 키(height)는 cm 단위, 몸무게(weight)는 kg 단위이다.
     이 자료를 이용하여 BMI 지수를 계산한 후 정상 범주의 인원수와 
     고도비만 범주의 인원수의 차의 절대값을 구하시오.
     
     조건1> BMI 지수 = 몸무게 / (키**2) 
           - 몸무게 단위 : kg
           - 키 단위 : m 
     조건2> 정상 범주 BMI 지수 :  18 ~ 25   
           고도비만 BMI 지수 :  30초과          
'''

# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\7_제5회_실전문제\data'
a = pd.read_csv(path +'/student.csv') 
a.info()
'''
 0   name    14 non-null     object
 1   height  14 non-null     int64 
 2   weight  14 non-null     int64 
''' 

df = a.copy() 
df['BMI'] = df['weight'] / (df['height'] * df['height']) *10000
target = len(df[(df['BMI'] >= 18) & (df['BMI'] <= 25)])

target2 = len(df[df['BMI'] > 30])

result = abs(target - target2)
print(result)
