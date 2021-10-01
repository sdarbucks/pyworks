# findAll() - 모든 태그 요소를 찾아서 리스트로 반환

from bs4 import BeautifulSoup

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

html = BeautifulSoup(html_str, "html.parser")

first_ul = html.find('ul', {'class':'item'})    # Dictionary 자료구조 {키:값}
all_li = first_ul.findAll('li')
print(all_li)