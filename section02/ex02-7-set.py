'''
파일명: ex02-7-set.py

Set
    고유한 원소로 구성된 변경 가능한 컬렉션 타입
    중복값을 허용하지 않는다.
    순서가 없다.
'''

thisset = {'피카츄','라이츄','파이리'}
print(thisset) # 실행할 때마다 순서가 바뀜

# set 길이
print(len(thisset))

# 항목 가져오기
for x in thisset:   # thisset 길이만큼 반복
    print(x)

# 값이 있는지 확인
thisset = {'피카츄','잠만보','메타몽'}
print('피카츄' in thisset)
print('꼬부기' in thisset)

# 항목 추가하기
thisset.add('꼬부기')
print(thisset)

# 중복값 테스트 => 테스트 결과 중복값 허용하지 않는다.
thisset.add('잠만보')
print(thisset)

# 다른 Set 항목 추가
thisset1 = {}