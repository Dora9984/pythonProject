'''
파일명: ex12-99-jackpot.py
'''

import random
import time

# [1, 2, 3, 4, 5, ... ,45]
pot = [n for n in range(1, 46)]

jackpot = []

for n in range(1, 7): # 1 ~ 6
    random.shuffle(pot) # 리스트 순서 섞는다

    pick = pot.pop()
    print(f'{n}번째 당첨번호는 {pick}입니다.')