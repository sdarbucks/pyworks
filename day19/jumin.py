#3
pin = "881120-3068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#4 성별 문자가 1, 3이면 '남자', 아니면 '여자'
print(pin[7])
if pin[7] == '1' or pin[7] == '3':
    print("남자")
else:
    print("여자")

#5
a = "a:b:c:d"
b = a.replace(':', '#')   #이전문자, 새문자
print(b)

#6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#7 리스트 -> 문자열 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
