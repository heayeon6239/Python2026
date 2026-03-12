# 파이썬 함수의 특징
# - 함수 생성시 반드시 def로 시작
# - 함수를 실행할 때는 함수이름을 호출
# - 매개변수 값을 전달할 때 함수이름(매개값)
# - 파이썬은 지역변수를 블록(for, if)등이 아니라 함수(def)기준으로 스코프(scope)가 나뉨

# 스코프(scope)란?
# 변수를 사용할 수 있는 범위 (전역변수를 함수(def)안에서 사용하려면 반드시 global 명령어 사용)

# 함수(def)에서 값을 return 받을 때 여러개인 경우 튜플을 사용
# def test() ~ return (a,b)

# 01. 함수
def print_address():
    print("종로구",end=" ")
    print("파이썬건물",end=" ")
    print("홍길동")

print_address() # 종로구 파이썬건물 홍길동

# 02. 함수에 매개변수 사용
def print_address(name):
    print("종로구",end=" ")
    print("파이썬건물",end=" ")
    print(name)

print_address("개나리") # 종로구 파이썬건물 개나리

# ==========================================================================

# 03. 함수값 반환
def cal_area(radius):
    area = 3.14 * radius ** 2 # area -> 지역변수
    return area

# print(area) -> 지역변수인 area를 전역으로 사용불가
cal = cal_area(5)
print(cal) # 78.5

# 04. 함수에 매개변수 여러개 전달
def get_sum(start, end):
    sum = 0
    for i in range(start,end+1):
        sum += i
    return sum

print(get_sum(1,10)) # 55

# 05. 함수의 매개변수를 input()으로 입력받아 결과값 출력하는 함수
def cal_area02(radius):
    result = 3.14 * radius ** 2
    return result

ra = int(input("반지름 입력: "))
print(cal_area02(ra)) # 78.5