# -*- coding: utf-8 -*- 

class Service:
  def __init__(self, name):
    self.name = name
    self.money = 0
  def change_name(self, name):
    self.name = name
  def save_income(self, money):
    self.money += money
  def save_expense(self, money):
    self.money -= money
  def say_my_name(self):
    print("%s님의 현재 재산은 %d원입니다." % (self.name, self.money))

me = Service("Yewon")
me.save_income(50000)
me.save_income(50000)
me.save_expense(10000)
me.save_income(50000)
me.say_my_name()