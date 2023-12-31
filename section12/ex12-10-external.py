'''
파일명: ex12-10-external.py

라이브러리 - 패키지 집합

패키지
    모듈의 상위 개념
    모듈의 집합을 의미한다.

pip - 패키지 관리자 도구
    PYPL(Python Package Index)에서 패키지를 다운로드한다.
    수많은 오픈소스가 저장되어 있는 중앙 저장소

패키지 설치
pip install 패키지명

패키지 삭제
pip uninstall 패키지명
'''

# 행렬 연산 관련 package
import numpy as np # numpy 설치가 안됨..

print(np.sum([1, 2, 3, 4, 5]))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 각 요소 더하기
c = a + b
print(c)
c = np.add(a, b)
print(c)

# 각 요소 빼기
c = a - b
c = np.subtract(a, b)
print(c)

# 각 요소 곱하기
c = a * b
c = np.multiply(a, b)
print(c)

# 각 요소 나누기
c = a / b
c = np.divide(a, b)
print(c)
