from class_calculator import Calculator

test = Calculator()
test.add(500)
test.say()
test.add(10000)
test.say()
test.add(200)
test.say()

# 모듈에 작성한 print() 같은 실행문도 다 실행된다.
# 다른 파일에서 모듈을 갖고올 때 
# 실행이 안되게하려면 모듈 내에 
# if __name__ == "__main__": 내에 실행문을 작성하면 된다.
