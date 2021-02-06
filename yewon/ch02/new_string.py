# -*- coding: utf-8 -*- 

str_doing = 'hardwork'
str_soyeon = 'soyeon did %s ' % str_doing
print(str_soyeon)

str_equal = '0000'
print('='.join(str_equal))

print('{0},{1}'.format('grape', 3000))
print('{fruit},{price}'.format(fruit='apple', price=2000))
print('{0}, {fruit}, {1}, {price}'.format('first', 'second', fruit='banana', price=2000))
# print('{0}, {2}, {1}, {3}'.format('first', 'second', fruit='banana', price=2000)) # error

# 정렬
print('{0:>7}'.format('12345'))
print('{0:<7}'.format('12345'))
print('{0:^7}'.format('12345'))

# 공백 채우기
print('{0:=>7}'.format('12345'))
print('{0:=<7}'.format('12345'))

# 소수
print('{0:5.2f}'.format(3.1425))

# { }
print("{{ and }}".format())