# 문제 8)
 
wish = int(input("목표 일 매출액: "))
weeks = ["월","화","수","목","금","토","일"]
max = 0
min = 999999999999
wishSuccess = 0
totalRevenue = 0

for week in weeks:
    revenue = int(input(f"{week}요일 매출: "))


    # 총 매출
    totalRevenue += revenue
    # 최고 매출
    if max < revenue:
        max = revenue # 매출액
        maxWeek = week # 요일
    # 최저 매출
    if min > revenue:
        min = revenue
        minWeek = week

    # 목표달성/분발필요/목표미달
    target = (revenue / wish) * 100
 
    if target >= 70 and target < 100:
        print("-> 분발 필요")
    elif target < 70:
        print("-> 목표 미달")
    else:
        print("-> 목표 달성")
        wishSuccess += 1

# 일평균
avg = int(totalRevenue / 7)

print(f"총 매출: {totalRevenue:,}원  |  일 평균: {avg:,}원")
print(f"최고 매출: {maxWeek}요일 {max:,}원  |  최저 매출: {minWeek}요일 {min:,}원")
print(f"목표 달성: {wishSuccess}일")

    
