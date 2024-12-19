import requests
## Import the BeautiFulSoup from  bs4(beautifulsoup4) Library
from bs4 import BeautifulSoup

## Assign URL / Sent GET request at Web server / Assing respons
url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

# Translate HTML that BeautifulSoup function parameter give and Generate BeautifulSoup Object
soup = BeautifulSoup(html_src,'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print('\n')
print(soup.body)
print('\n')

print('title 태그 요소:',soup.title)
# print('title 태그 이름:',soup.title.name)
# print('title 태그 문자열:',soup.title.string)
