'''
파일명 : ex08-3-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''
total = 0
for a in range(1,101):
    if a % 3 == 0:  # 3의 배수
        continue    # 아래 코드를 skip 하고 위의 for 문으로 돌아감
    total += a
    print(f'a: {a}, total {total}')

print(total)