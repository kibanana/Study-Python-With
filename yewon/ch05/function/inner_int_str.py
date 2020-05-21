# chr()
print(chr(63)) # ?
print(chr(65)) # A
print(chr(97)) # a

# ord()
print(ord('?')) # 63
print(ord('A')) # 65
print(ord('a')) # 97

# eval()
print(eval('1 + 3')) # 4
print(eval('5 * 50')) # 250
print(eval('divmod(50, 3)')) # (16, 2)

# int()
# print(int('2.0')) # 에러 발생
print(int(5.5)) # Math.floor()한 값과 같다
print(int('6'))
print(int('0xff', 16))

# str()
print(str(3))
print(str('hi' + ',' + 'hello'))
print(str('hi'.upper()))