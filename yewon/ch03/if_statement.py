# -*- coding: utf-8 -*- 

sleepy = True
if sleepy is True:
  print('나 잔다')
else:
  print('나 안잔다')

prac_number = 0
prac_string = ""
prac_list = []
prac_tuple = ()
prac_dictionary = {}

if prac_number:
  print('number')

if prac_string:
  print('string')

if prac_list:
  print('list')

if prac_tuple:
  print('tuple')

if prac_dictionary:
  print('dictionary')


if not prac_number:
  print('Not number')

if not prac_string:
  print('Not string')

if not prac_list:
  print('Not list')

if not prac_tuple:
  print('Not tuple')

if not prac_dictionary:
  print('Not dictionary')

prac_list_true = [1]
prac_tuple_true = (1)
prac_string_true = 'hello'

if 1 in prac_list_true:
  print('It\'s true list')

# TypeError: argument of type 'int' is not iterable
# if 1 in prac_tuple_true:
#  print('It\'s true tuple')

if 'l' in prac_string_true:
  print('It includes "l"')

pocket = ['car key', 'phone']
if 'money' in pocket:
  print('내 주머니에 돈있다')
elif 'car key' in pocket:
  print('내 주머니에 차키있다')
elif 'phone' in pocket:
  print('내 주머니에 폰있다')