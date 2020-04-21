# 1
# 'need'

# 2
i = 0
while True:
  i += 1
  if i > 5: break
  print('*' * i)

# 3
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in A:
  total += i
average = total / len(A)
print(average)