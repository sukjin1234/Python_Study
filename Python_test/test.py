import re

s = "Jian777 is very famous Data scientist. He is only 26 years old byt published 19 papers."

# 숫자가 포함되지 않은 단어 찾기 (영문+숫자는 제외)
print(re.findall(r"\b[A-Za-z]+\b", s))  
print(re.findall(r"\b[A-Za-z]+\b",s))
# 숫자만 포함된 부분 찾기
print(re.findall(r"\b\d+\b", s))
print(re.findall(r"\b\d+\b",s))

# 영문+숫자 조합 찾기
print(re.findall(r"\b[A-Za-z]+\d+\b", s))
print(re.findall(r"\b[A-Za-z]+\d+\b", s))

