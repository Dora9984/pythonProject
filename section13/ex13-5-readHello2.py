'''
파일명: ex13-5-readHello2.py

file 객채 read() 함수
    read() -> 전체 읽어오기
    read(인자값) -> 인자값 크기만큼 읽어오기
'''
with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.read(5)
        if not str:
            break
        print(str)