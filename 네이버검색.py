import requests
import csv
import key

# 네이버 API 클라이언트 ID와 Secret
client_id = key.getNaverKey()[0]
client_secret = key.getNaverKey()[1]

# 검색 쿼리 설정 (노원구 빌라 전월세)
query = '노원구 부동산'
url = f'https://openapi.naver.com/v1/search/blog?query={query}'

# API 요청 헤더 설정
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

# API 요청
response = requests.get(url, headers=headers)

# 응답 처리
if response.status_code == 200:
    data = response.json()

    # CSV 파일로 저장
    with open('villa_rent_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # CSV 헤더 작성
        writer.writerow(['Title', 'Link', 'Description', 'Blogger Name', 'Post Date'])

        # 검색 결과 저장
        for item in data['items']:
            title = item['title']
            link = item['link']
            description = item['description']
            bloggername = item['bloggername']
            postdate = item['postdate']
            writer.writerow([title, link, description, bloggername, postdate])

    print("CSV 파일로 저장되었습니다.")
else:
    print(f"Error Code: {response.status_code}")
