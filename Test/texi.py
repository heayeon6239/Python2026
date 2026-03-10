Departure = input("출발지 입력: ")
Arrival = input("도착지 입력: ")
km = float(input("이동거리 입력: "))
time = int(input("탑승시간 입력: "))
child = input("어린이 동반 여부: 예/아니오")

# 계산

# 거리요금
over = int(((km - 2)* 1000)/100 *100)
if km > 2 and child == "아니오":
    baseFare = 4800
else:
    baseFare = 0

# 총 금액
if time >= 22 or time <= 4:
    # 심야할증
    nightFare = 0.2
    night = int((baseFare + over) * nightFare)
    total = baseFare + over + night
else:
    total = baseFare + over
    night = 0


print("="*40)
print("택시 요금 안내")
print("="*40)

print(f"출발지\t:{Departure}")
print(f"도착지\t:{Arrival}")
print(f"이동거리\t:{km}Km")
print(f"탑승시간\t:{time}시")
print("="*40)

# 기본요금
print(f"기본요금\t:{baseFare:>10,}원")
# 거리요금
print(f"거리요금\t:{over:>10,}원")
# 심야할증
print(f"심야할증\t:{night:>10,}원 (20% 적용)")
print("-"*40)

# 최종요금
print(f"최종요금\t:{total:>10,}원")
print("="*40)