# 문제 01)
products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]

print("=== 재고 현황 ===")

total = 0

# ★ 배열의 길이 -> len(products)
for i in range(len(products)):
    product = products[i]
    stock = stocks[i]

    total += stocks[i]

    if stocks[i] < 10:
        note = "재고 부족"
    else:
        note = ""
    # -> 출력하는 변수 msg이용한 버전
    # ★ 문자와 숫자는 한줄로 나열 X -> str()함수로 숫자를 문자열로 변환
    msg = product + ":" + str(stock) + "개" 
    print(msg)
    # -> f-String 사용 버전
    # print(f"{products[i]}:{stocks[i]}개 {note}")

print()
print(f"전체 재고 합계: {total}개")
