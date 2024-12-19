import requests, re
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

links = soup.find_all("a")
print("하이퍼링크의 개수:", len(links))
print("\n")
print("첫 3개의 원소:", links[:3])
print("\n")