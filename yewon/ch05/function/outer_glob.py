from glob import glob
import os
# 파일 I/O 기능이 있는 프로그램을 만들 때 특정 디렉터리에 있는 파일 이름을 모두 알아야할 때가 있다.

filenames = glob(os.getcwd() + "\\*")
print(filenames)