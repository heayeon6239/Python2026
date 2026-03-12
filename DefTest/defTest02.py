# 함수 안에서 전역변수 사용하기
def cal_area(radius):
    # ★ 전역변수로 담겼기 때문에 area를 return 하지 않아도 됨
    global area
    area = 3.14 * radius ** 2
    return # 종료의 의미(없어도)

area = 0 # 전역변수
r = float(input("반지름 입력: "))
cal_area(r)
print(area) # 78.5

