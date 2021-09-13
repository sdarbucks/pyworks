# 숫자 포맷팅으로 파일 쓰기 - 연산 가능
f  = open("c:/pyfile/number.txt", 'w')
f.write("%d\n" % (100*2))

f.close()
