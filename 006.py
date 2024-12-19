import requests
from bs4 import BeautifulSoup


## Extract HTML source code of Web page &
url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name = 'img', attrs={'alt':'Seoul Metro 2000 series train on Line 2'})
print('HTML 요소', target_img)
print("\n")

target_img_src = target_img.get('src')
print('이미지 파일 경로',target_img_src)
print("\n")

target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "./output/download_image.jpg"

with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장.")