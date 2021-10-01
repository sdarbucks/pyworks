# find() - 처음 나오는 태그 요소를 찾아옴

from bs4 import BeautifulSoup # BeautifulSoup 모듈 - HTML과 XML 문서를 파싱(분석)하기 위한 파이썬 라이브러리

html_str = '''
<html>
    <body>
        <ul class = 'item'>
            <li>인공지능</li>
            <li>Big Data</li>
            <li>로봇</li>
        </ul>
        <ul class = 'comlang'>
            <li>Python</li>
            <li>C/C#</li>
            <li>Java</li>
        </ul>
    </body>
</html>
'''

html = BeautifulSoup(html_str, "html.parser")   # html.parser - 분석기 명
first_ul = html.find('ul')
print(first_ul)
print(first_ul.text)
