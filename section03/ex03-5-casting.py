'''
파일명 : ex03-5-casting.py

형변환(casting)
    변수에 유형을 지정하려는 경우 캐스팅으로 가능
'''

# 정수형
x = int(1)
print(x)
y = int(2.8)
print(y)
z = int("3")
print(z)
z2 = "3"
print(x+z)
print(str(x) + z2)
print(x + int(z2))

# 실수형
x = float(1)
print(x)
z = float("3")
print(z)

# 문자형
x = str(1)
y = str(2)
print(x + y) # 문자열 + 문자열 = 문자 연결

# 아스키 코드 변환
a = ord('A')
print(a)
b = chr(65)
print(b)

