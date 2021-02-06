# -*- coding: utf-8 -*- 

from calendar import calendar, prcal, prmonth, weekday, monthrange

# 일 년 달력 보기
print(calendar(2020, 5)) # 좀 더 크게 보이지만 별다를바 없다
print(calendar(2020))
print(prcal(2020))

# 월 달력 보기
print(prmonth(2020, 5))

# 월요일: 0
print(weekday(2020, 5, 22))

# 요일과 그 달이 며칠까지있는지
print(monthrange(2020, 5)) # (4, 31) -> 금요일, 5월은 31일까지 있다