name = input("이름 입력:")
ko = int(input("국어 점수:"))
En = int(input("영어 점수:"))
ma = int(input("수학 점수:"))

# 계산
total = ko + En + ma
avg = float(total/3)

print("-"*60)
print(f"이름: {name}점")
print(f"국어: {ko}점")
print(f"영어: {En}점")
print(f"수학: {ma}점")
print("-"*60)

print(f"총점: {total}점")
print(f"평균: {avg:.2f}점")
if ko < 40 or En < 40 or ma < 40:
    print("학점: F")
elif avg >= 90:
    print("학점: A")
elif 90 > avg >= 80:
    print("학점: B")
elif 80 > avg >= 70:
    print("학점: C")
elif 70 > avg >= 60:
    print("학점: D")
else :
    print("학점: F")