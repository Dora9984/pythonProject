'''
파일명: ex11-7-variable-local-global2.py
'''

gVar = '전역'

def gloablAndLocal():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(f'{gVar} 변수입니다.')
    print(f'{lVar} 변수입니다.')

gloablAndLocal()
print(gVar)
