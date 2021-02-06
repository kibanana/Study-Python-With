# -*- coding: utf-8 -*- 

import sys

args = sys.argv[1:] # argv[0]은 실행 시 입력하는 파일명이다
for i in args:
	print(i, type(i))