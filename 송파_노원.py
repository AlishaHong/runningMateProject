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

# print(df_nowon_2024_1.shape)
# print(df_nowon_2024_1.columns)
# print(df_nowon_2024_2.shape)
# print(df_nowon_2024_2.columns)
# print(df_nowon_2024_3.shape)
# print(df_nowon_2024_3.columns)

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

# print(df_songpa_2022_1.info())
# 송파_단독다가구
# 종전계약 보증금/월세 데이터가 있는 행만 뽑아서 구별 보증금/월세 인상률 확인해보기(송파_단독다가구의 경우 1090행)
# 건축년도 정보가 나름 중요해보이는데 5910/6152 결측치 200개 -> 어떻게 해야 좋을지 

# print(df_songpa_2022_2.info())
# 송파_연립다세대 
# 종전계약보증금/월세(6008/18677) 제외하고는 결측치 없음 

# print(df_songpa_2022_3.info())
# 송파_오피스텔
# 종전계약보증금/월세(1935/6646)
# 건축년도(6269/6646)





# 연립다세대에서 본번,부번 삭제 
# 단독다가구에서 도로조건 삭제 

# 연립다세대 - 전용면적 / 단독다가구 - 계약면적  : 컬럼명 통일하기 

# 연립다세대에는 층 정보가 있는데 필요한 컬럼이니까 단독다가구에 층 컬럼을 추가해서 1층으로 채우는게 나을 것 같음 

# 그 외에 갱신요구권 종전계약 보증금 등 당장 필요하지 않고 결측치가 많은 컬럼은 삭제하자 
# 연립다가구는 괜찮은데 단독 다가구는 건축년도와 도로명 결측치가 꽤 있다. 
# 도로명은 지번 주소로 대체가능하니 삭제해도 되겠지만 건축년도는 필요해보임.. 







# 지하철역과의 거리에 따른 집값 분석
# 노원구 지하철역 :
# 태릉입구역,화랑대역(서울여대입구역),봉화산역,갈매역,공릉역(서울과학기술대역)
# 하계역,중계역,노원역,상계역,당고개역,마들역,수락산역


# 지오코딩으로 각 도로명 주소를 위도 경도로 변환 
# 노원구에 위치한 지하철 및 인근 구의 지하철역의 주소를 가져온뒤
# 집과 각 역의 거리를 계산하여 가장 가까운 역을 기준으로 역세권 여부를 범주화 한다. 




# 크키별 평균 전세금 구하기 
# 송파구와 노원구 같은 범주에서 비교해보기 


# 1. 노원구 2022년 단독 다가구 
# print(df_nowon_2022_1.head())
# print(df_nowon_2022_1.tail())
노원구_단독다가구_전세 = df_nowon_2022_1[df_nowon_2022_1['전월세구분'] == '전세']
# print(노원구_단독다가구_전세)
# print(len(노원구_단독다가구_전세))
노원구_단독다가구_전세 = 노원구_단독다가구_전세.reset_index(drop=True)

# 계약면적 중 가장 큰값과 가장 작은값 추출 
가장넓은집 = 노원구_단독다가구_전세['계약면적(㎡)'].idxmax()
가장좁은집 = 노원구_단독다가구_전세['계약면적(㎡)'].idxmin()

print(노원구_단독다가구_전세.iloc[가장넓은집])
# print(노원구_단독다가구_전세.iloc[가장좁은집])


# 집 크기 범주화 함수
def categorize_size(size):
    if size < 40:
        return '소형'
    elif 40 <= size < 80:
        return '중형'
    else:
        return '대형'

# 면적을 기준으로 집 크기 범주화
df_nowon_2022_1['크기_범주'] = df_nowon_2022_1['계약면적(㎡)'].apply(categorize_size)
노원구_단독다가구_전세['크기_범주'] = 노원구_단독다가구_전세['계약면적(㎡)'].apply(categorize_size)

# 크기범주 별 전세 평균 금액 
# 크기범주 별 월세 평균 금액


# 에러발생(결측치나 문자열이 있는지 확인)
# 에러코드를 보면 object 타입이어서 그런듯 
# 숫자형으로 바꾼 뒤 계산해보자 

# 결측치 여부 확인(없음)
print(노원구_단독다가구_전세['보증금(만원)'].isnull().sum)
# 보증금에 콤마가 들어가있음 콤마제거하기 
노원구_단독다가구_전세['보증금(만원)'] = 노원구_단독다가구_전세['보증금(만원)'].str.replace(',','')
# 숫자형으로 변환
노원구_단독다가구_전세['보증금(만원)'] = 노원구_단독다가구_전세['보증금(만원)'].astype(int)

print(노원구_단독다가구_전세.groupby('크기_범주')['보증금(만원)'].mean().round(2))




# 2. 송파구 2022년 단독다가구 

송파구_단독다가구_전세 = df_songpa_2022_1[df_songpa_2022_1['전월세구분'] == '전세']

송파구_단독다가구_전세 = 송파구_단독다가구_전세.reset_index(drop=True)

# 계약면적 중 가장 큰값과 가장 작은값 추출 
가장넓은집 = 송파구_단독다가구_전세['계약면적(㎡)'].idxmax()
가장좁은집 = 송파구_단독다가구_전세['계약면적(㎡)'].idxmin()

print(f'가장넓은집 : {송파구_단독다가구_전세.iloc[가장넓은집]}')
# print(f'가장좁은집 : {송파구_단독다가구_전세.iloc[가장좁은집]}')


# 집 크기 범주화 함수
def categorize_size(size):
    if size < 40:
        return '소형'
    elif 40 <= size < 80:
        return '중형'
    else:
        return '대형'

# 면적을 기준으로 집 크기 범주화
df_songpa_2022_1['크기_범주'] = df_songpa_2022_1['계약면적(㎡)'].apply(categorize_size)
송파구_단독다가구_전세['크기_범주'] = 송파구_단독다가구_전세['계약면적(㎡)'].apply(categorize_size)
# 결과 출력
# print(df_songpa_2022_1)
# print(송파구_단독다가구_전세)


# 에러발생(결측치나 문자열이 있는지 확인)
# 에러코드를 보면 object 타입이어서 그런듯 
# 숫자형으로 바꾼 뒤 계산해보자 



# 결측치 여부 확인(없음)
# print(송파구_단독다가구_전세['보증금(만원)'].isnull().sum)

# 보증금에 콤마가 들어가있음 콤마제거하기 
송파구_단독다가구_전세['보증금(만원)'] = 송파구_단독다가구_전세['보증금(만원)'].str.replace(',','')
# 숫자형으로 변환
송파구_단독다가구_전세['보증금(만원)'] = 송파구_단독다가구_전세['보증금(만원)'].astype(int)

print(송파구_단독다가구_전세.groupby('크기_범주')['보증금(만원)'].mean().round(2))

# 각 범주별 개수 세기
송파구_단독다가구_전세_크기_개수 = 송파구_단독다가구_전세['크기_범주'].value_counts()
노원구_단독다가구_전세_크기_개수 = 노원구_단독다가구_전세['크기_범주'].value_counts()

print(송파구_단독다가구_전세_크기_개수)
print(노원구_단독다가구_전세_크기_개수)
# 크기범주 별 전세 평균 금액 
# 크기범주 별 월세 평균 금액

print(df_songpa_2022_1)
# '월세' 열이 있는지 확인하고, 월세를 전세로 변환
def convert_to_jeonse(row):
    row['보증금(만원)'] = row['보증금(만원)'].replace(',', '')
    row['보증금(만원)'] = pd.to_numeric(row['보증금(만원)'], errors='coerce')

    if pd.notna(row['월세금(만원)']):  # 월세 값이 있는 경우
        additional_deposit = (row['월세금(만원)'] // 5) * 1000  # 월세를 보증금으로 변환 (5만원당 보증금 500)
        row['보증금(만원)'] += additional_deposit  # 기존 보증금에 추가
        row['월세금(만원)'] = 0  # 월세를 0으로 설정 (전세로 변환)
        row['전월세구분'] = '전세'
    return row


# print(df_songpa_2022_1.info())
# 데이터프레임에 변환 적용
df_songpa_2022_1_converted = df_songpa_2022_1.apply(convert_to_jeonse, axis=1)

# 수정된 데이터 확인 후 새로운 CSV 파일로 저장
df_songpa_2022_1_converted.to_csv('modified_rental_data.csv', index=False)

print("모든 월세 매물이 전세로 변환되었습니다.")

modified_rental_data = pd.read_csv('modified_rental_data.csv')
print(modified_rental_data.info())
print(modified_rental_data.head())


# 소형~중형평수만 확인하기(청년층 주거지) 5480/6152
data_for_youth = modified_rental_data[modified_rental_data['계약면적(㎡)'] < 60.00]
print(data_for_youth.info())
print(data_for_youth.head())

print(data_for_youth['보증금(만원)'].mean().round(2))

data_for_youth.to_csv('data_for_youth.csv', index=False)

# 도로명 주소가 있는 데이터를 가지고 위도경도 변환해보기 
#geopy 패키지
#주소값을 위경도로 변환

# 가입 없이 주소->좌표 변환
# from geopy.geocoders import Nominatim

# 주소나 위도, 경도가 중복되지 않은 고유한 정보를
# 리스트에 각각 담아주기 위해 빈 리스트 생성

# unique_lat=[]
# unique_lng=[]
# except_addr=[]


#지오코딩
#주소를 마커나 지도를 배치하는데 사용할 수 있는 지리좌표로 변환하는 과정

#역지오코딩 
#지리좌표를 사람이 읽을 수 있는 주소로 변환 

# 주소를 위도와 경도로 변환해 주는 함수
# def geocoding(address):
#     geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)    #사용자 에이전트 설정
#     geo = geolocoder.geocode(address)   #주소로 위치정보 가져오기(위도와 경도 반환)
#     # 주소값을 제대로 인식하지 못할때
#     # 위도와 경도값을 None값을 리턴한다.
#     if geo==None:
#         print(f'주소가 어디인지 인식할 수 없습니다.: {address}')
#         except_addr.append(address)
#         return 0, 0
#     else:
#         return geo.latitude, geo.longitude  #위도,경도
    
# map_addr = data_for_youth['도로명']

# for addr in map_addr:
#     lat, lng = geocoding(addr)
#     unique_lat.append(lat)
#     unique_lng.append(lng)
    

# print(unique_lat, unique_lng)



# [송파구 2022 단독다가구]
# Name: 보증금(만원), Length: 1839, dtype: bool>
# 크기_범주32
# 대형    30020.44
# 소형    11007.87
# 중형    18845.71

# [노원구 2022 단독다가구]
# Name: 보증금(만원), Length: 1056, dtype: bool>
# 크기_범주
# 대형    19884.94
# 소형     7374.45
# 중형    12764.03


# [송파구 2022 단독다가구 크기별 카운트]
# 크기_범주
# 소형    888
# 중형    798
# 대형    153
# Name: count, dtype: int64

# [노원구 2022 단독다가구 크기별 카운트]
# 크기_범주
# 소형    633
# 중형    340
# 대형     83
# Name: count, dtype: int64

# 도로명 결측치가 있는 행은 제거 

map_addr_all = data_for_youth['도로명'].dropna()
map_addr1 = map_addr_all.head(3000)
map_addr2= map_addr_all.iloc[3000:]
map_addr1.to_csv('map_addr1.csv', index = False)
map_addr2.to_csv('map_addr2.csv', index = False)


