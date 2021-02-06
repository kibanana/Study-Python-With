# -*- coding: utf-8 -*- 

def safe_sum_check(a, b):
  if type(a) != type(b):
    print("더할 수 없는 값들입니다.")
    return
  else:
    return (a + b)