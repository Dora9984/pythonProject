'''
파일명: ex13-2-makeHello.py

open() 함수 모드
    w(write mode) : 쓰기 전용 모드 / 파일이 없으면 생성
    t(text mode) : 해당 파일의 데이터를 텍스트 파일로 인식하고 입출력

'''

file = open('hello.txt','wt', encoding='UTF-8')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
file.write('hello.txt 파일이 생성되었습니다.')
file.close()

