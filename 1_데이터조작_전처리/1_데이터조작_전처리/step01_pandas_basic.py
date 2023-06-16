# -*- coding: utf-8 -*-
"""
빅분기 pandas 기초 문법 
 - 자료 조작 & 자료 통계 
"""

import pandas as pd
path = r'C:\ITWILL\7_BigGisa\1_데이터조작_전처리\data'
a = pd.read_csv(path +'/mtcars.csv') 
a.info() # total 11 columns
 

# 1.DataFrame 복제와 자료형 변환  
df = a.copy() # 내용 복제 


''' 
자료형 변환
 형식) df.칼럼 = df.칼럼.astype(자료형) 
'''
df.hp = df.hp.astype('float64') # int64 -> float64 변환 
df.info() 


# 2. DataFrame 행/열 삭제 
'''
   형식) df.drop(index, axis=0) : 행 삭제 
   형식) df.drop(['칼럼1','칼럼2'], axis=1) : 열 삭제 
'''
# 1) 행 삭제 
df.drop([0,2,4], axis=0) # 0, 2, 4 index 제거 
ndf = df.drop([0,2,4], axis=0) # 새로운 객체 생성
 
 
# 2) 열 삭제 
df.drop(['drat', 'am'], axis=1) # default : axis=0 
df.drop(['drat', 'am'], axis=1, inplace=True) # 현재 객체 반영 


# 3. DataFrame 행/열 추출과 추가 
'''
  형식) row = df.iloc[index] : 행 추출 
  형식) df.iloc[index] = 값 : 행 추가 
  형식) df['칼럼'] = 값 : 열 추가 
'''

# 1) 행 추출과 추가 
row = df.iloc[0] # index 0행 추출 
df.index # RangeIndex(start=0, stop=32, step=1)
df.iloc[30] = row # index 30행 덮어쓰기 


# 2) 열 추출과 추가 
mpg = df.mpg # 칼럼 추출 
df['mpg2'] = mpg # 칼럼 추가 


# 3) 상위 70% 추출
ndf = df.head(int(len(df) * 0.7)) 
print(ndf) 


# 4) 특정 칼럼값의 50% 이상 추출 
des = df['mpg'].describe() # mpg 칼럼 기준 
ratio50 = des['50%'] 

ndf = df[df['mpg'] >= ratio50]
ndf.shape 


# 4. 중복행 제거와 칼럼 유일값  
df.info() # RangeIndex: 32 entries, 0 to 31
df = df.drop_duplicates()
df.info() # Int64Index: 31 entries, 0 to 31

# vs 칼럼 기준 
df.vs.unique() # array([0, 1], dtype=int64)
df.vs.value_counts()



# 5. 조건으로 행 or 열 선택  

''' 
  형식) df[df.칼럼 관계식]
'''
df[df.vs == 1] # 1일 때 
df[df.vs < 1] # 0 일 때 

'''
논리연산자(&, |) 조건으로 행 선택
  형식) df[(df.칼럼 관계식) 논리식 (df.칼럼 관계식)]
'''
df.gear.unique() # gear변수 유일값([4, 3, 5]) 

df[(df.vs==1) & (df.gear==4)] # v=1이고 gear=4인 행 추출 
df[(df.vs==0) | (df.gear>4)] # v=0이거나 gear=5인 행 추출 

''' 
컬럼 조건으로 특정 열 선택 
  형식) df.loc[df.칼럼 관계식, ['칼럼','칼럼']]
'''
# vs==1 일 때 mpg, disp 칼럼 추출 
df.loc[df.vs == 1, ['mpg','disp']] # v=1 일때 mpg, disp 칼럼 추출 

''' 
두 개 이상 칼럼 선택 
  형식) df[['칼럼', '칼럼']]
'''
df[['mpg', 'disp', 'gear']] # 콜론(:) 사용 불가 


# 6. 데이터프레임 행, 열 합치기 

# 1) DF 생성 
df.info()

df1 = df.iloc[:, :4]
df2 = df.iloc[:, 4:]
df1.info()
df2.info()

# 2) DF 공통 칼럼 추가 
uid = range(len(df)) # 0 ~ 31
df1['uid'] = uid # 칼럼 추가 
df2['uid'] = uid # 칼럼 추가 

# 3) 공통 칼럼으로 병합(merge) 
df3 = pd.merge(left=df1, right=df2, on='uid')
df3.info() 


# 4) 열 단위 결합  
df_con = pd.concat([df1, df2], axis=1)
df_con.info() 


# 5) 행 단위 결합  
df_con2 = pd.concat([df1,df2], axis=0, ignore_index=True) # 행 이름 무시 
df_con2



# 7. 칼럼, 인덱스 변경 
'''컬럼, 인덱스 이름 변경'''
df.rename(columns={'mpg':'MPG'}, index={0:'zero'}, inplace=True)
print(df)

'''행 인덱스 초기화'''
df = df.reset_index()
print(df) # index 칼럼 추가 
df.drop('index',axis=1, inplace=True) # index 칼럼 제거 
print(df)


''' 특정 칼럼을 인덱스로 적용'''
df1.set_index('uid', inplace=True)
print(df1)
df1 = df1.reset_index() # 원위치 
print(df1)


# 8. 정렬 : 색인, 칼럼 
''' 인덱스로 정렬 '''
df = df.sort_index(ascending=False) # 색인 내림차순 
df = df.sort_index() # ascending=True 생략 가능 


''' 특정 칼럼값으로 정렬'''
ndf = df.sort_values('wt',ascending=False) # wt열 기준 내림차순 정렬
print(ndf)


# 9. 요약통계량 
print(ndf.describe())

# 사분위수 추출 : MPG 칼럼 기준 
des = ndf.describe() 
result = des.loc['25%', 'MPG']
print(result) # 0.4616519174041298

result = des.loc['75%', 'MPG']
print(result) # 0.672566371681416


# 10. 그룹별 통계
df['gear'].unique() # array([4, 3, 5], dtype=int64)

gear_grp = df.groupby('gear') # 그룹 객체 
gear_grp.size() # 그룹 개수 


# 그룹별 평균  
gear_grp.mean() # gear그룹별 전체 컬럼 평균 
gear_grp['cyl'].mean() # 그룹별 특정 칼럼(cyl) 평균 


# 그릅별 요약통계 
gear_grp.describe() # gear그룹별 전체 칼럼 요약통계 
gear_grp['cyl'].describe() # 그룹별 특정 칼럼(cyl) 요약통계 







