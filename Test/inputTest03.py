name = input("이름을 입력하세요:")
cm = int(input("키를 입력하세요(cm):"))
kg = int(input("현재 체중을 입력하세요(kg):"))

cal = float((cm - 100) * 0.9)
cal2 = float(kg / cal * 100)

print("-"*50)
print(f"{name}님의 비만도는 {cal2:.2f}% 입니다.")
print("-"*50)
