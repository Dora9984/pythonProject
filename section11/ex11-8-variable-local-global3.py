'''
파일명: ex11-8-variable-local-global3.py

pythontutor.com/render.html#mode=display <- 전역, 지역변수 이해에 참고
'''
# 전역변수 선언
total = 0

def gift(dic,who,money):
    global total
    total += money
    dic[who] = money

wedding = {}
name = '영희'
gift(wedding, name, 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 10)
print(f'축의금 명단: {wedding}')
print(f'전체 축의금: {total}')
