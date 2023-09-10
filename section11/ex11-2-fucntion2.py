'''
파일명: ex11-2-fucntion2.py
'''
# 매개변수 o, 리턴 x -> 매개변수 입력값을 받아 실행하는 함수
def introduce(name,age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('박은비', 24)
introduce('피닉스', 22)

# 가변 매개변수 함수
def show(*args):
    print(type(args))
    for item in args:
        print(item)

show('Python')
show('Python', 'Java', 'C++', 'Ruby', 'Go')