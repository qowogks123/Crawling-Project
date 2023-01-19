s = '제 생일은 9월 입니다'

#arr = s.split('생일은 ')
#s = arr[1]

#print(s.split('월')[0])


birth_day = s.split('생일은 ')[1].split('월')[0]
print(birth_day)
#print(s.find('e'))

#pos = s.find('생일은 ')
#pos += 4

#print(s[pos:pos+1])