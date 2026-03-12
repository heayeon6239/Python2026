# 문제 03)

member_data = [
    {"name": "김철수", "age": 20},
    {"name": "이영희", "age": 25},
    {"name": "박민수", "age": 18}
]

def filter_members(age):
    global result
    result = []
    for data in member_data:
        if data['age'] >= age:
            result.append(data['name'])
        
input_age = int(input("나이 입력: "))
filter_members(input_age) # 함수 실행
print(f"{input_age}이상 회원 : {result}")




