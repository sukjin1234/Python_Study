# 정규식 : 특정한 규칙을 가지고 있는 문자열들을 표현하는데 사용되는 규칙을 가진 언어

import re
# re.search() 정규식에 매치되는 문자열을 찾을 수 있다.
txt1 = 'Life is too short, you need python'
txt2 = 'The best moments of my life'
txt3 = 'My Life my Choice'
print(re.search('Life',txt1))
print(re.search('Life',txt2))

match = re.search('Life',txt1)
print(match.group()) # 문자열 출력
print(match.start()) # 문자열 시작 위치
print(match.end()) # 문자열 끝 위치
print(match.span()) # 문자열 위치 (시작, 끝)

print(re.search('Life|life',txt2)) # | : or(또는)

print(re.search('[Ll]ife',txt2)) # [] : 문자 선택의 범위를 표현
# [], |, -, ^, $ ... : 메타문자

print(re.search("^Life",txt1))  # ^ : 제일 첫 단어로 나오는지 검사
print(re.search("^Life",txt2))
print(re.search("^Life",txt3))

print(re.search('life$',txt1)) # $ : 가장 마지막 단어로 나오는지 검사
print(re.search('life$',txt2))

print(re.search('A..A','ABA')) # . : 임의의 한개 문자 
print(re.search('A..A','ABBA'))

print(re.search('AB*','A'))  # * : * 직전에 있는 문자가 0회 이상 반복되면 일치
print(re.search('AB*','AA')) # 'A'라는 문자열이 조건에 맞음
print(re.search('AB*','CABBA')) # 'ABB' 라는 조건에 맞음
print(re.search('AB*','B'))

print(re.search('AB?','A')) # ? : ? 직전에 있는 문자를 0회 또는 1회 반복한 패턴에 매치
print(re.search('AB?','AA'))
print(re.search('AB?','X-MAN')) # 'A'라는 조건에 맞음
print(re.search('AB?','CABBA')) # 'AB'라는 조건에 맞음

print(re.search('AB+','A')) # + : + 직전에 있는 패턴을 1회 또는 그 이상의 수로 반복하는 패턴에 매치
print(re.search('AB+','ABB'))

# findall() : 정규식을 만족하는 모든 문자열을 추출
print(re.findall('[Mm]y',txt3))

# \d : 숫자와 문자와 매치되는 문자열을 추출하는 방법 

# \b : 숫자가 포함되지 않은 단어만 찾도록 제한

re.sub('찾을문자','변경할문자',변수명)

'''
import re
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
email = re.findall("\S+@[a-z.]+",txt)
print(email)
'''

print(re.findall(r"\d\d\d\d"))
                # r은 정규식에서 \를 한 번만 적어도 되게 해줌줌