######################################
# 제1유형-6 : 데이터 처리 & 통계
######################################

# 유형6 : 날짜형 자료 처리 
# 제출 : print(result) 

''' 
 문) 2015년10월 1개월 동안 Volume이 100,000 보다 크고(>) 
     200,000 보다 작은(<) 레코드 수를 출력하시오.(제4회 실기 문제)
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path + '/sam_kospi.csv')
print(a)
'''
          Date     Open     High      Low    Close  Volume
0    30-Oct-15  1345000  1390000  1341000  1372000  498776
1    29-Oct-15  1330000  1392000  1324000  1325000  622336
2    28-Oct-15  1294000  1308000  1291000  1308000  257374
3    27-Oct-15  1282000  1299000  1281000  1298000  131144
4    26-Oct-15  1298000  1298000  1272000  1292000  151996
'''
a.info()

# 1. 날짜형 변환 : Object -> Date형  
a['kdate'] = pd.to_datetime(a['Date'])
a.info() # 6   kdate   247 non-null    datetime64[ns]

dir(a['kdate'].dt) # dt 속성 메서드 
'''
day, month, year, hour, minute, second
'''

# 2. 날짜형 변수 -> 월 추출 
a['month'] = a['kdate'].dt.month
a.info()

# 2015~2020

# 3. 2015년 10월 자료 추출 
df = a[a['month'] == 10]
df.shape # (21, 8)

# 4. Volume : 100,000 보다 크고 200,000 보다 작은 레코드
result = df[(df['Volume'] > 100000) & (df['Volume'] < 200000)]
result.shape  # (8, 8)



