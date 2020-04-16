# 1
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 2
pin = '881120-1068234'
print(pin[7:8])

# 3
a = [1,3,5,4,2]
a.sort()
# a.sort(reverse=True)
a.reverse()
print(a)

# 4
a = ['Life','is','too','short']
result = ' '.join(a)
print(result)

# 5
a = (1,2,3)
a = a + (4,)
print(a)

# 6
a = {
  'A': 90,
  'B': 80,
  'C': 70
}
result = a.pop('B')
print(a)
print(result)

# 7
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 8
a = b = [1,2,3]
a[1] = 4
print(b)

# 두 변수가 같은 객체를 가리키고 있기 때문에