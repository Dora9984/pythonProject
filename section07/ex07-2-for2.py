'''
파일명: ex07-2-for2.py

'''
# 문자와 숫자를 조합해서 만들어야 하는 비밀번호
pwd = input('비밀번호를 입력하세요 >>> ')

ch_count = 0
num_count = 0
for ch in pwd:
    if ch.isalpha():    # 문자값이 입력되면 True -> 실행
        ch_count += 1
    elif ch.isnumeric():    # 숫자값이 입력되면 True -> 실행
        num_count += 1
if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호입니다.')