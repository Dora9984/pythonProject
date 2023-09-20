'''
파일명: ex14-1-copyFile.py

파일복사
    원본 읽기 -> 버퍼(Memory 저장) -> 복사본 쓰기

opne() 함수 모드
    b(binary mode):
        해당 파일의 데이터를 바이너리 파일로 인식하고 입출력.
'''

buffer_size = 1024  # 1024byte -> 1kb
with open('../section13/hello.txt','rb') as source: # source가 hello.txt 파일이라고 봐도 됨
    with open('hello2.txt','wb') as copy: # copy가 hello2.txt 파일
        while True:
            buffer = source.read(buffer_size) # source에서 데이터를 읽어오는 것
            if not buffer:
                break
            copy.write(buffer) # source에서 읽어온 데이터를 copy에 복사하는 것

print('hello2.txt 파일이 복사되었습니다.')