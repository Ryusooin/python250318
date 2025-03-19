# DemoStr.py
#문자열 메소드 연습
strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA)) #문자열 길이
print(len(strB))
print(strA.capitalize()) #대문자로 변환

data = " spam and ham "
result = data.strip() #양쪽 공백 제거
print(data)
print(result)

result = result.replace("spam", "spam and egg") #문자열 치환
print(result)
lst = result.split("and") #문자열 분리
print(lst)
result = ":".join(lst) #문자열 결합
print(result)


#정규표현식
import re

result = re.search("[0-9]")