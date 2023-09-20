'''
파일명: ex14-3-csvWriter.py
'''

import csv

# 첫번재 방법
'''
with open('차량관리.csv', 'w', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2023-06-11,12:00'])
    csv_maker.writerow([2, '02다1234', '2023-06-11,12:00'])
    csv_maker.writerow([3, '28하1234', '2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')
'''

# 두번째 방법
'''
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2023-06-11,12:00'])
    csv_maker.writerow([2, '02다1234', '2023-06-11,12:00'])
    csv_maker.writerow([3, '28하1234', '2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')
'''

# 세번째 방법
with open('차량관리.csv', 'w', newline='', encoding='UTF-8') as file:
    csv_maker = csv.writer(file, delimiter=',') # 세번째 값에 "가 안붙으면 quotechar='"' 추가("가 붙는게 디폴트)
    csv_maker.writerow([1, '08러1234', '2023-06-11,12:00'])
    csv_maker.writerow([2, '02다1234', '2023-06-11,12:00'])
    csv_maker.writerow([3, '28하1234', '2023-06-11,12:00'])

print('차량관리.csv 파일이 생성되었습니다.')