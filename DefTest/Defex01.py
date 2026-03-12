# 문제 01)

books = [("파이썬 기초", 15000), ("자바의 정석", 25000), ("React 입문", 18000)]

print("--- 도서 목록 ---")
for book in books:
    print(f"도서명: {book[0]}, 가격: {book[1]:,}원")

def total_price():
    global total
    total = 0
    for book in books:
        total += book[1]

print()
print(f"전체 도서 합계: {total:,}원")

