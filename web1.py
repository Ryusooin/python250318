# web1.py
#웹크롤링 코드를 작성
from bs4 import BeautifulSoup

#웹페이지 로딩
page = open("c:\\work\\Chap09_test.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")

#<p>태그 전부 검색
print(soup.find_all("p"))