rest_coffee = 10
while True: # 무한루프
  money = int(input('돈을 넣어주세요 : '))
  if not rest_coffee:
    print('커피 다 떨어졌습니다! 판매 중지합니다.')
    break
  if money > 300:
    print('커피 받으세요! 거스름돈 %d 받으세요!' % (money - 300))
    rest_coffee -= 1
  elif money == 300:
    print('커피 받으세요!')
    rest_coffee -= 1
  else:
    print('돈 돌려드릴게요! 커피 안드릴거임!')