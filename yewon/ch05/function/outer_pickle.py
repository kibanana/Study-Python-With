# -*- coding: utf-8 -*- 

import pickle

# with open("test.txt", "wb") as f: # write binary
#  어떤 자료형이든 상관없다.
#   data = {
#     1: 'Python',
#     2: 'Flask',
#     3: 'Django',
#   }
#   pickle.dump(data, f)
#   f.close()

with open("test.txt", "rb") as f:
  data = pickle.load(f)
  print(data)
  f.close()