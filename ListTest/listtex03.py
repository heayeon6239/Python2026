# 문제 03)
orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'},
]


print("=== 결제 완료 주문 ===")

totalPay = 0
cart = []

# PAID만 cart 담기
for order in orders:
    if order['status'] == "PAID":
        cart.append(order)
        totalPay += order['amount']

# cart 출력
for pro in cart:
    print(f"{pro['id']}번 주문 / 상품: {pro['product']} / 금액: {pro['amount']:,}원")

print()
print(f"총 결제 금액: {totalPay:,}원")