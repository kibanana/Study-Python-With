def gugu(n):
  result = []
  for i in range(1, 10):
    result.append(n * i)
  return result

n = input("구구단 몇 단? : ")
print(gugu(int(n)))