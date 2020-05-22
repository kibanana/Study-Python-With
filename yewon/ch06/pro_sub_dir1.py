import os

def search(dirname):
  try:
    filenames = os.listdir(dirname)
    for filename in filenames:
      full_filename = os.path.join(dirname, filename)
      if os.path.isdir(full_filename):
        search(full_filename) # 디렉터리면 재귀적으로 search 호출
      else: # 디렉터리가 아니면 -> 파일이면
        ext = os.path.splitext(filename)[-1]
        if ext == ".txt":
          print(full_filename)
  except PermissionError: # 권한이 없는 디렉터리에 접근해도 프로그램이 원활히 계속되도록 한다.
    pass

os.chdir("../")
search(os.getcwd())