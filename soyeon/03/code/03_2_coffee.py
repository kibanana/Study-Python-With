#coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어주세요:"))
    if money ==300:
        print("커피를 줍니다")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다")%(money-300))
        coffee = coffee -1
    
