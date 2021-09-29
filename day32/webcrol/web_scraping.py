# urllib 모듈로 웹 스크레이핑하기

from urllib import request

contents = request.urlopen("https://www.naver.com/")
print(contents.read())
