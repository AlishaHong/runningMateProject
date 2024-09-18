import requests
from bs4 import BeautifulSoup
import pandas as pd

# 사이트맵 파일 목록
sitemaps = [
    "https://kbland.kr/sitemap1.xml",
    "https://kbland.kr/sitemap2.xml",
    "https://kbland.kr/sitemap3.xml",
    "https://kbland.kr/sitemap4.xml",
    "https://kbland.kr/static/kbland/sitemap/sitemap5.xml",
    "https://kbland.kr/static/kbland/sitemap/sitemap6.xml",
    "https://kbland.kr/static/kbland/sitemap/sitemap7.xml"
]

# 각 사이트맵 파일에서 URL을 추출하는 함수
def extract_urls_from_sitemap(sitemap_url):
    try:
        print(f"사이트맵에서 URL 추출 중: {sitemap_url}")
        response = requests.get(sitemap_url, timeout=40)  # 타임아웃 설정
        soup = BeautifulSoup(response.content, 'xml')
        urls = [loc.text for loc in soup.find_all('loc')]
        print(f"{len(urls)}개의 URL을 추출했습니다.")
        return urls
    except requests.exceptions.Timeout:
        print(f"타임아웃 발생: {sitemap_url}")
        return []

# 모든 사이트맵에서 URL을 추출
all_urls = []
for sitemap in sitemaps:
    urls = extract_urls_from_sitemap(sitemap)
    all_urls.extend(urls)

# 매물 정보를 추출하는 함수 (노원구 지역 매물만 추출)
def extract_mw_info(page_url, target_location):
    try:
        print(f"매물 정보 추출 중: {page_url}")
        response = requests.get(page_url, timeout=10)  # 타임아웃 설정
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 페이지에서 지역 정보를 추출 (예: '서울 노원구')
        location = soup.find('div', class_='location').text.strip() if soup.find('div', class_='location') else "N/A"
        
        # 노원구에 해당하는 매물만 필터링
        if target_location in location:
            title = soup.find('h1', class_='title').text.strip() if soup.find('h1', class_='title') else "N/A"
            price = soup.find('div', class_='price').text.strip() if soup.find('div', class_='price') else "N/A"
            print(f"매물 발견: {title}, 가격: {price}, 위치: {location}")
            
            return {
                'URL': page_url,
                'Title': title,
                'Price': price,
                'Location': location
            }
        else:
            print(f"노원구 매물이 아닙니다: {location}")
            return None
    except requests.exceptions.Timeout:
        print(f"타임아웃 발생: {page_url}")
        return None

# 전월세 매물 정보를 저장할 리스트
mw_list = []

# 노원구 지역 설정
target_location = "노원구"

# 모든 페이지에서 매물 정보 추출
for url in all_urls:
    mw_info = extract_mw_info(url, target_location)
    if mw_info:  # 매물 정보가 노원구에 해당하면 리스트에 추가
        mw_list.append(mw_info)

# pandas DataFrame으로 변환
df = pd.DataFrame(mw_list)

# CSV 파일로 저장
df.to_csv('매물_정보_노원구.csv', encoding='utf-8-sig', index=False)

print(f"{target_location} 지역에 해당하는 매물 정보가 CSV 파일로 저장되었습니다.")




# Sitemap: https://kbland.kr/sitemap_index.xml
# User-agent: bingbot
# Crawl-delay: 30

# User-agent: *
# Allow: /
