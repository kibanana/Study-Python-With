# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.

def encrypt(s):
  rule = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
  result = ""
  encryption_list = list(map(str, s.split(" "))) # split()에 인수 안넣고 실행하면 모든 공백이 사라진다.
  for i in encryption_list:
    if i == "":
      result += " "
    else:
      idx = rule.index(i)
      result += chr(65 + idx)
  return result

encryption = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
print(encrypt(encryption))
