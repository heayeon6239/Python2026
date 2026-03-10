
movie_no = "2026-0309-01"
movie = "7관 (4층)"
movieName = "파이썬의 습격"
time = "14:30 ~ 16:10"

people1,price1,quan1 = "일반 성인",15000,2
people2,price2,quan2 = "청소년",10000,1

# 계산
pe1 = price1 * quan1
pe2 = price2 * quan2
total = pe1 + pe2

print("="*60)
print(f"{"PYTHON CINEMA":^45}")
print("="*60)

print(f"티켓번호: {movie_no}")
print(f"상영관: {movie}")
print(f"영화명: {movieName}")
print(f"상영시간: {time}")

print("-"*60)
print(f"{"구분":<20} {"단가":>10} {"인원":>5} {"금액":>10}")
print("-"*60)
print(f"{people1:<24} {price1:<11,} {quan1:<9} {pe1:<0,}")
print(f"{people2:<25} {price2:<11,} {quan2:<9} {pe2:<0,}")
print("-"*60)
print(f"{"총 결제 금액"} {total:>44,}")
print("="*60)
