# 문제 05)
transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]

month = {}
monthTotal = 0

# ★ a,b =10,20 가능 ★
for date, amount in transactions:
    if date in month:
        month[date] += amount

# 월별 매출 계산
for tran in transactions:
    # 해당 월이 존재하면 +매출, 아니면 생성 (딕셔너리 사용시 존재 확인 필요)
    if tran[0] in month:
        month[tran[0]] += tran[1]
    else:
        month[tran[0]] = tran[1]

# 최고 매출
max = 0
for tran in month.keys():
    if month[tran] > max:
        max = month[tran]
        maxMonth = tran

# 최저 매출
min = max
for tran in month.keys():
    if month[tran] < min:
        min = month[tran]
        minMonth = tran

# 평균
total = 0
for tran in month.keys():
    total += month[tran]

avg = int(total / len(month))

# 출력
print("=== 월별 매출 ===")
for tran in month.keys():
    print(f"{tran} : {month[tran]:,}원")

print()
print(f"최고 매출 월: {maxMonth} ({max:,}원)")
print(f"최저 매출 월: {minMonth} ({min:,}원)")
print(f"월 평균 매출: {avg:,}원")