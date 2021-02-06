# -*- coding: utf-8 -*- 

import os

def search(dirname):
  # f = os.popen("dir")
  # data = f.read()
  
  result = []
  filenames = os.listdir(dirname)
  for filename in filenames:
    result.append(os.path.join(dirname, filename))
  return result

print(search(os.getcwd()))

print()
print()
print("=" * 50)
print()
print()

os.chdir("../") # 상위 디렉터리
print(search(os.getcwd()))

print()
print()
print("=" * 50)
print()
print()

def search_txt(dirname):
  result = []
  filenames = os.listdir(dirname)
  for filename in filenames:
    full_filename = os.path.join(dirname, filename)
    ext = os.path.splitext(full_filename)[-1]
    if ext == ".txt":
      result.append(full_filename)
  return result

print(search_txt(os.getcwd()))