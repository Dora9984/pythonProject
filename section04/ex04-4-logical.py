'''
파일명: ex04-4-logical.py

논리 연산자
    관계 연산자와 함께 사용되는 연산자로
    2개 이상의 항을 논리적으로 연결할 때 사용한다.

    and : 2개항 모두 True 일 때 True
    or : 2개항 어느 한 쪽이 True 일 때 True
    not : 논리 값을 반전시킨다.
'''

a = 10
b = 0
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0))
print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b > 0))

print('not {} : {}'.format(a, not a)) # not a 는 0의 값이 아닌 정수값으로 True
print('not {} : {}'.format(b, not b)) # 0 -> False