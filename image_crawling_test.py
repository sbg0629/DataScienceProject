import requests
from bs4 import BeautifulSoup
import urllib

def save_images(search_term, num_images):
    # 검색어로 이미지 검색
    url = f"https://www.google.com/search?q={search_term}&tbm=isch"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 이미지 URL 추출
    image_elements = soup.find_all("img", limit=num_images)
    image_urls = [element["src"] for element in image_elements]
    
    # 이미지 다운로드
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # 이미지 파일 저장
            with open(f"book{i}.png", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
                    
            print(f"이미지 {i+1}/{num_images} 다운로드 완료.")
        
        except Exception as e:
            print(f"이미지 다운로드 실패: {e}")
        
        if i+1 >= num_images:
            break