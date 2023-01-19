# beautifulsoup 주요 기능

"""
- html 문자열 파싱
- html 노드 인식 및 편리한 기능들
- parent, children, contents, descendants, sibling
- string, strings, strippend_strings, get_text()
- prettify
- html attribute 
"""
# html글자를인식해서 사용하기 편하게 해주는 것이 beautifulsoup
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser")

print(soup.title)
