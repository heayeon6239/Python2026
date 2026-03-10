name = input("이름 입력:")
pay = int(input("시급 입력:"))
dayWorkTime = float(input("하루 근무 시간(h):"))
day = int(input("근무 일수:"))
startTime = int(input("근무 시작 시간:"))

# 계산

# 야간근무
if startTime >= 22 or startTime <= 6:
    nightPay = int(pay * 1.5)
     # 야간수당 시급
    dayPay = nightPay
    word = "해당 있음"
else:
    # 시급
    dayPay = pay
    nightPay = 0
    word = "해당 없음"

# 총 근무시간(근무시간 * 근무일수)
AllWorkTime = dayWorkTime * day

# 기본급여
basePay = int(AllWorkTime * dayPay)

# 주휴수당
if AllWorkTime >= 15:
    overTime = int(dayWorkTime * dayPay) # 주휴수당
    word2 = "해당 있음"
else:
    overTime = 0
    word2 = "해당 없음"

# 총 급여(총 근무 시간 * 시급)
totalPay = AllWorkTime * dayPay + overTime

# 세금
tax = int(totalPay * (3.3 / 100))

# 실수령액
netPay = int(totalPay - tax)


print("="*40)
print("급여 명세서")
print("="*40)

print(f"이름\t:{name}")
print(f"시급\t:{pay:,}원")
print(f"근무시간\t:{AllWorkTime} (8.0h * 5일)")
print(f"야간근무\t:{word} (시급 {nightPay:<,}원 적용)")
print(f"주휴수당\t:{word2}")
print("="*40)

print(f"기본급\t:{basePay:<,}원")
print(f"주휴수당\t:{overTime:<,}원")
print(f"세금(3.3%)\t:{tax:<,}원")
print("-"*40)

print(f"실수령액\t:{netPay:<,}원")


