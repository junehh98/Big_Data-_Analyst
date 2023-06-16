######################################
# 제1유형-3 : 데이터 처리 & 통계
######################################

# 유형3 : 자료변형과 조건색인  
# 제출 : print(result) 

'''
 문) disp를 정규화한 후 0.25 이상이고 0.6 미만인 레코드에서 cyl 평균과 
    0.65 초과하고 0.8 미만인 레코드에서 cyl 평균과의 차이를 절댓값으로 구하시오.
'''


# 데이터 파일 읽기 예제
import pandas as pd
path = r'C:\ITWILL\7_BigGisa\4_제1유형\data'
a = pd.read_csv(path +'/mtcars.csv')  


import sklearn 
dir(sklearn) # 호출 가능 모듈 확인 
print(sklearn.__all__)
'''
ensemble : RandomForest 
model_selection : train/test split
metrics : 평가도구 
preprocessing : 전처리 도구(스케일링, 인코딩) 
'''

import sklearn.preprocessing 
# 모듈의 호출가능한 함수 or 클래스 
dir(sklearn.preprocessing)
'''
MinMaxScaler
StandardScaler
OneHotEncoder
LabelEncoder
'''


# 1) 정규화 
from sklearn.preprocessing import MinMaxScaler 

# 스케일링 : 주의) fit_transform(2D)
a['disp_scaled'] = MinMaxScaler().fit_transform(a['disp'].to_frame())

# 2) 조건에 맞는 자료 추출 : 0.25 이상이고 0.6 미만
disp_result = a[(a['disp_scaled'] >= 0.25) & (a['disp_scaled'] < 0.6)] 
disp_result.shape # (7, 12)

# 3) cyl 평균 
cyl_avg1 = disp_result['cyl'].mean() 


# 4) 조건에 맞는 자료 추출 : 0.65 초과하고 0.8 미만
disp_result2 = a[(a['disp_scaled'] > 0.65) & (a['disp_scaled'] < 0.8)] 
disp_result2.shape # (4, 12)

# 5) cyl 평균 
cyl_avg2 = disp_result2['cyl'].mean() 

# 6) 평균의 차(절댓값) 계산 
result = abs(cyl_avg1 - cyl_avg2)
print(result) # 0.5714285714285712












