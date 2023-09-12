'''
파일명: ex12-4-module4.py

별명 사용하기
    as(alias) 키워드 사용
'''

import converter as cvt

miles = cvt.kilometer_to_miles(150)
print(f'150km = {miles}miles')