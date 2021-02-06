# -*- coding: utf-8 -*- 

from webbrowser import open, open_new, open_new_tab

# 웹브라우저가 이미 실행된 상태면 주소로 이동하고,
# 웹브라우저가 실행되지 않은 상태면 새로운 웹브라우저를 실행하고 주소로 이동한다.
open("http://google.com/")

# 웹브라우저가 이미 실행되었어도 새로운 웹브라우저를 실행하고 주소로 이동한다.
open_new("http://naver.com/")

open_new_tab("http://daum.net/")