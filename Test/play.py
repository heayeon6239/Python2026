month = int(input("방문 월 입력:"))
adult = int(input("성인 인원수 입력:"))
teen = int(input("청소년 인원수 입력:"))
kid = int(input("어린이 인원수 입력:"))
senior = int(input("경로 인원수 입력:"))

# 계산

# 가격
adultPrice = 55000 * adult
teenPrice = 40000 * teen
seniorPrice = 15000 * senior

# 총 인원수
totalPeoNum = adult + teen + kid + senior

# 비성수기 할인
if month in [7,8]:
    monthDiscount = 0
    monthWord = "성수기"
    monthDiscountWord = ""
else:
    monthWord = "비수기"
    if totalPeoNum >= 5:
        monthDiscount = 0.1
        monthDiscountWord = "(10%)"

# 어린이 동반 할인    
if kid >= 3:
    kidPrice = 0
    kidWord = "(무료!)"
else:
    kidPrice = 28000 * kid
    kidWord = ""

# 소계
total = adultPrice + teenPrice + kidPrice + seniorPrice

# 할인금액
discountPrice = int(total * monthDiscount) 

# 최종금액
netPay = total - discountPrice

print("="*40)
print("놀이공원 입장서 계산서")
print("="*40)

print(f"{month}월 ({monthWord})")
print("="*40)
print(f"성인\t{adult}명:\t{adultPrice:,}원")
print(f"청소년\t{teen}명:\t{teenPrice:,}원")
print(f"어린이\t{kid}명:\t{kidPrice:,}원 {kidWord}")
print(f"경로\t{senior}명:\t{seniorPrice:,}원")
print("="*40)

print(f"소계\t: {total:,}원")
print(f"단체할인\t: -{discountPrice:,}원 {monthDiscountWord}")
print("="*40)

print(f"최종금액\t: {netPay:,}원")
print("="*40)
print(f"총 인원\t: {totalPeoNum}명")