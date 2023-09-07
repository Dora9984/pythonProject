'''
파일명: ex06-4-while4.py
'''

dan = 2
while dan < 9:  # dan:2 n:1 -> 2X1=2 n:2 -> 2X2=4 ... 2X9
    n = 1
    while n <= 9:
        print(f'{dan}X{n}={dan*n}', end=' ')
        n += 1
    dan += 1
    print()