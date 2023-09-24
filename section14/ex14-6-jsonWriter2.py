'''
파일명: ex14-6-jsonWriter2.py
'''

import json

dict_list = [
    {
        'name':'james',
        'age':20,
        'spec':[
            175.5,
            70.5
        ]
    },
    {
        'name':'홍길동',
        'age':21,
        'spec':[
            182.5,
            79.5
        ]
    }

]

# indent 들여쓰기, ensure_ascii=False 한글읽기 가능하다
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
print(json_string)

with open('dictList.json', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다.')