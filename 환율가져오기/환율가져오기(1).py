import requests as req

res = req.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

html = res.text
s = html.split('<span class="value">')[1].split('</span>')[0]
print(s)

#pos = html.find('배재한')
#print(pos)
# find는 데이터가 있는지 없는지 확인할때 사용 

import re

#s = 'colour'
#print(re.match(r'colou?r', s))

#s = "how are you?"
#print(re.match(r'how are you\?',s))

# A B C F
#s = '이 영화는 E등급 입니다.'
#print(re.match(r'이 영화는 [ABC.]등급 입니다', s))

s = '이 영화는 F등급 입니다'
print(s.split('이 영화는')[1].split('등급')[0])
print(re.findall(r'이 (..)는 (.)등급 입니다', s))