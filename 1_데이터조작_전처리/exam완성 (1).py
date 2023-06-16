# -*- coding: utf-8 -*-
"""
문) 다음과 같은 iris 자료를 대상으로 데이터 인코딩과 스케일링을 수행하시오.
     단계1> 1~4번 칼럼 : 표준화(StandardScaler) 스케일링 
     단계2> 5번 칼럼 :  레이블 인코딩(label encoding)
     단계3> 두 개의 결과를 하나의 DataFrame으로 만들어서 new_df 생성 
     단계4> new_df의 상위 30%를 대상으로 3번 칼럼(petal_length)의 제3사분위수 출력
      
"""
import seaborn as sn # dataset load  
import pandas as pd  # DataFrame 생성 
# 전처리 도구 
from sklearn.preprocessing import StandardScaler, LabelEncoder

iris = sn.load_dataset('iris')
iris.info()
'''
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object
'''

# 변수 선택 
X = iris.iloc[:, :4]
'''
X = iris[['sepal_length','sepal_width','petal_length','petal_width']]
'''
y = iris.species


# 1. 스케일링 
X_scaled = StandardScaler().fit_transform(X = X) # 2d 자료 
X_scaled

# 2. 인코딩 
y_encoding = LabelEncoder().fit_transform(y = y) # 1d 자료 
y_encoding


# 3. DataFrame 생성 
new_df = pd.DataFrame(X_scaled)
new_df['species'] = y_encoding 

# 칼럼명 지정 
new_df.columns = iris.columns 
new_df.info()


# 4. 상위 30% -> 3번 칼럼(petal_length) 제3사분위수
new_df2 = new_df.head(int(len(new_df) * 0.3))
new_df2.shape # (45, 5)

petal_length = new_df2.petal_length
des = petal_length.describe() # 요약통계 
print(des['75%']) # -1.226551672795556













