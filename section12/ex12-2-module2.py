'''
파일명: ex12-2-module2.py

모듈 사용법
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2

'''

from converter import kilometer_to_miles

miles = kilometer_to_miles(150)
print(f'150km = {miles}miles')