'''
파일명: ex14-2-csvReader.py

CSV(comma-separated values)
    필드를 쉼표(,)로 구분한 텍스트 파일
'''

student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
        
print(student_list)