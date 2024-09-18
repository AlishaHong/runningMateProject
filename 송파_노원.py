import pandas as pd

# 데이터 읽어오기  

# 1. 단독다가구
# 2. 연립다세대
# 3. 오피스텔
songpa_2022_1 = pd.read_csv('data_송파/송파구_단독다가구_2022.csv', encoding='utf-8')
songpa_2022_2 = pd.read_csv('data_송파/송파구_연립다세대_2022.csv', encoding='utf-8')
songpa_2022_3 = pd.read_csv('data_송파/송파구_오피스텔_2022.csv', encoding='utf-8')

songpa_2023_1 = pd.read_csv('data_송파/송파구_단독다가구_2023.csv', encoding='utf-8')
songpa_2023_2 = pd.read_csv('data_송파/송파구_연립다세대_2023.csv', encoding='utf-8')
songpa_2023_3 = pd.read_csv('data_송파/송파구_오피스텔_2023.csv', encoding='utf-8')

songpa_2024_1 = pd.read_csv('data_송파/송파구_단독다가구_2024.csv', encoding='utf-8')
songpa_2024_2 = pd.read_csv('data_송파/송파구_연립다세대_2024.csv', encoding='utf-8')
songpa_2024_3 = pd.read_csv('data_송파/송파구_오피스텔_2024.csv', encoding='utf-8')


nowon_2022_1 = pd.read_csv('data_노원/노원구_단독다가구_2022.csv', encoding='utf-8')
nowon_2022_2 = pd.read_csv('data_노원/노원구_연립다세대_2022.csv', encoding='utf-8')
nowon_2022_3 = pd.read_csv('data_노원/노원구_오피스텔_2022.csv', encoding='utf-8')

nowon_2023_1 = pd.read_csv('data_노원/노원구_단독다가구_2023.csv', encoding='utf-8')
nowon_2023_2 = pd.read_csv('data_노원/노원구_연립다세대_2023.csv', encoding='utf-8')
nowon_2023_3 = pd.read_csv('data_노원/노원구_오피스텔_2023.csv', encoding='utf-8')

nowon_2024_1 = pd.read_csv('data_노원/노원구_단독다가구_2024.csv', encoding='utf-8')
nowon_2024_2 = pd.read_csv('data_노원/노원구_연립다세대_2024.csv', encoding='utf-8')
nowon_2024_3 = pd.read_csv('data_노원/노원구_오피스텔_2024.csv', encoding='utf-8')





# 송파구

df_songpa_2022_1 = pd.DataFrame(songpa_2022_1)
df_songpa_2022_2 = pd.DataFrame(songpa_2022_2)
df_songpa_2022_3 = pd.DataFrame(songpa_2022_3)
df_songpa_2023_1 = pd.DataFrame(songpa_2023_1)
df_songpa_2023_2 = pd.DataFrame(songpa_2023_2)
df_songpa_2023_3 = pd.DataFrame(songpa_2023_3)
df_songpa_2024_1 = pd.DataFrame(songpa_2024_1)
df_songpa_2024_2 = pd.DataFrame(songpa_2024_2)
df_songpa_2024_3 = pd.DataFrame(songpa_2024_3)

# print(df_songpa_2022_1.shape)
# print(df_songpa_2022_1.columns)
# print(df_songpa_2022_2.shape)
# print(df_songpa_2022_2.columns)
# print(df_songpa_2022_3.shape)
# print(df_songpa_2022_3.columns)

# 송파 2022년 

# 단독다가구
# Index(['NO', '시군구', '번지', '도로조건', '계약면적(㎡)', '전월세구분', '계약년월', '계약일', '보증금(만원)',
#        '월세금(만원)', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용', '종전계약 보증금(만원)',
#        '종전계약 월세(만원)', '주택유형']
# (6152,18)
# 연립다세대
# Index(['NO', '시군구', '번지', '본번', '부번', '건물명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#        '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#        '종전계약 보증금(만원)', '종전계약 월세(만원)', '주택유형']
# (18677,21)
# 오피스텔
# Index(['NO', '시군구', '번지', '본번', '부번', '단지명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#        '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#        '종전계약 보증금(만원)', '종전계약 월세(만원)'],
#       dtype='object')
# (6646,20)


# print(df_songpa_2023_1.shape)
# print(df_songpa_2023_1.columns)
# print(df_songpa_2023_2.shape)
# print(df_songpa_2023_2.columns)
# print(df_songpa_2023_3.shape)
# print(df_songpa_2023_3.columns)


# 송파 2023년 

# 단독다가구 
# Index(['NO', '시군구', '번지', '도로조건', '계약면적(㎡)', '전월세구분', '계약년월', '계약일', '보증금(만원)',
#        '월세금(만원)', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용', '종전계약 보증금(만원)',
#        '종전계약 월세(만원)', '주택유형'],
#       dtype='object')
# (5246,18)

# 연립다세대 
# Index(['NO', '시군구', '번지', '본번', '부번', '건물명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#        '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#        '종전계약 보증금(만원)', '종전계약 월세(만원)', '주택유형'],
#       dtype='object')
# (17377,21)

# 오피스텔 
# Index(['NO', '시군구', '번지', '본번', '부번', '단지명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#        '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#        '종전계약 보증금(만원)', '종전계약 월세(만원)'],
#       dtype='object')
# (6349,20)


# print(df_songpa_2024_1.shape)
# print(df_songpa_2024_1.columns)
# print(df_songpa_2024_2.shape)
# print(df_songpa_2024_2.columns)
# print(df_songpa_2024_3.shape)
# print(df_songpa_2024_3.columns)

# 송파 2024년 

# 단독다가구 
# Index(['NO', '시군구', '번지', '도로조건', '계약면적(㎡)', '전월세구분', '계약년월', '계약일', '보증금(만원)',
#        '월세금(만원)', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용', '종전계약 보증금(만원)',
#        '종전계약 월세(만원)', '주택유형'],
#       dtype='object')
# (3502,18)

# 연립다세대 
# Index(['NO', '시군구', '번지', '본번', '부번', '건물명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#        '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#        '종전계약 보증금(만원)', '종전계약 월세(만원)', '주택유형'],
#       dtype='object')
# (12184,21)

# 오피스텔
#Index(['NO', '시군구', '번지', '본번', '부번', '단지명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#       '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#       '종전계약 보증금(만원)', '종전계약 월세(만원)'],
#      dtype='object')
# (4535,20)





# 노원구 

df_nowon_2022_1 = pd.DataFrame(nowon_2022_1)
df_nowon_2022_2 = pd.DataFrame(nowon_2022_2)
df_nowon_2022_3 = pd.DataFrame(nowon_2022_3)
df_nowon_2023_1 = pd.DataFrame(nowon_2023_1)
df_nowon_2023_2 = pd.DataFrame(nowon_2023_2)
df_nowon_2023_3 = pd.DataFrame(nowon_2023_3)
df_nowon_2024_1 = pd.DataFrame(nowon_2024_1)
df_nowon_2024_2 = pd.DataFrame(nowon_2024_2)
df_nowon_2024_3 = pd.DataFrame(nowon_2024_3)



# 노원 2022년 

# print(df_nowon_2022_1.shape)
# print(df_nowon_2022_1.columns)
# print(df_nowon_2022_2.shape)
# print(df_nowon_2022_2.columns)
# print(df_nowon_2022_3.shape)
# print(df_nowon_2022_3.columns)

# 단독다가구 
# Index(['NO', '시군구', '번지', '도로조건', '계약면적(㎡)', '전월세구분', '계약년월', '계약일', '보증금(만원)',
#      '월세금(만원)', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용', '종전계약 보증금(만원)',
#       '종전계약 월세(만원)', '주택유형'],
#      dtype='object')
# (3337, 18)

# 연립다세대 
# Index(['NO', '시군구', '번지', '본번', '부번', '건물명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#       '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#       '종전계약 보증금(만원)', '종전계약 월세(만원)', '주택유형'],
#      dtype='object')
# (2113, 21)

# 오피스텔
# Index(['NO', '시군구', '번지', '본번', '부번', '단지명', '전월세구분', '전용면적(㎡)', '계약년월', '계약일',
#       '보증금(만원)', '월세금(만원)', '층', '건축년도', '도로명', '계약기간', '계약구분', '갱신요구권 사용',
#       '종전계약 보증금(만원)', '종전계약 월세(만원)'],
#      dtype='object')
# (423, 20)



# 노원 2023년 

# print(df_nowon_2023_1.shape)
# print(df_nowon_2023_1.columns)
# print(df_nowon_2023_2.shape)
# print(df_nowon_2023_2.columns)
# print(df_nowon_2023_3.shape)
# print(df_nowon_2023_3.columns)

# 단독다가구 
# (3156, 18)

# 연립다세대 
# (1942, 21)

# 오피스텔 
# (556, 20)


# 노원 2024년 

print(df_nowon_2024_1.shape)
print(df_nowon_2024_1.columns)
print(df_nowon_2024_2.shape)
print(df_nowon_2024_2.columns)
print(df_nowon_2024_3.shape)
print(df_nowon_2024_3.columns)

# 단독다가구 
# (2176, 18)

# 연립다세대 
# (1292, 21)

# 오피스텔 
# (329, 20)



# info()로 결측치 많은 컬럼 확인하기
# 컬럼명 통일하기 
# 불필요한 컬럼 삭제 
# 구별로 합치기 
# 연도별로 합치기 
# 어떻게 비교하는것이 좋을지 생각해보기 







# 연립다세대에서 본번,부번 삭제 
# 단독다가구에서 도로조건 삭제 

# 연립다세대 - 전용면적 / 단독다가구 - 계약면적  : 컬럼명 통일하기 

# 연립다세대에는 층 정보가 있는데 필요한 컬럼이니까 단독다가구에 층 컬럼을 추가해서 1층으로 채우는게 나을 것 같음 

# 그 외에 갱신요구권 종전계약 보증금 등 당장 필요하지 않고 결측치가 많은 컬럼은 삭제하자 
# 연립다가구는 괜찮은데 단독 다가구는 건축년도와 도로명 결측치가 꽤 있다. 
# 도로명은 지번 주소로 대체가능하니 삭제해도 되겠지만 건축년도는 필요해보임.. 