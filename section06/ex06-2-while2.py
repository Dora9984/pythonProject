'''
파일명: ex06-2-while2.py
'''

my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> ' ))
while n != 0:
    my_list.append(n) # list에 n 값을 입력
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))

print(my_list)
