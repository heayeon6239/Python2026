# 문제 6)

cnt = 0
totalPurchase = 0
totalDiscount = 0
totalPay = 0
ok =  True

while True:
    # 초기화
    ok =  True
    
    # 등급입력
    level = input("회원 등급 (END 종료): ").upper()

    # END
    if level == "END":
        break
    # 예외처리
    elif level not in ["BRONZE","SILVER","GOLD","VIP"]:
        print("등록되지 않은 등급입니다.")
        ok = False

    if ok:
        # 구매금액
        purchase = int(input("구매금액: "))

        # BRONZE
        if level == "BRONZE":
            discount = 0
            pay = purchase
            cnt += 1
        # SILVER
        elif level == "SILVER":
            discount = int(purchase * 0.05)
            pay = purchase - discount
            cnt += 1
        # GOLD
        elif level == "GOLD":
            discount = int(purchase * 0.1 + 5000)
            pay = purchase - discount
            cnt += 1
        # VIP
        elif level == "VIP":
            discount = int(purchase * 0.2 + 10000)
            pay = purchase - discount
            cnt += 1

        print(f"할인금액: {discount}원 -> 결제금액: {pay}원")
        
        # 총 구매금액
        totalPurchase += purchase
        # 총 할인
        totalDiscount += discount
        # 총 결제금액
        totalPay += pay



print("--- 전체 주문 요약 ---")
print(f"주문 건수: {cnt}건")
print(f"총 구매금액: {totalPurchase:,}원")
print(f"총 할인금액: {totalDiscount:,}원")
print(f"총 결제금액: {totalPay:,}원")

    