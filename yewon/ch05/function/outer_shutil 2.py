# -*- coding: utf-8 -*- 

import shutil

# 파일을 복사한다.

shutil.copy("mkdir.txt", "m.txt") # 만약 dst의 값이 디렉터리고 src라는 파일 이름이 이미 존재한다면 덮어쓴다.
