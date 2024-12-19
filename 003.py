import requests

urls = ["https://www.naver.com/","https://www.python.org/"]
filename = "robots.txt"

for url in urls:
    file_path = url + filename
    print(filename)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")