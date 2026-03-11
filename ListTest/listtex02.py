# 문제 02)
member = {
    'name' : '김파이썬',
    'email' : 'python@example.com',
    'age' : 28,
    'grade' : 'GOLD'
}

print("=== 회원 정보 ===")

for key in member.keys():
    print(f"{key}: {member[key]}")

    # 등급
    if key == "age":
        if member[key] < 20:
            level = "주니어"
        elif 20 <= member[key] < 40:
            level = "일반"
        else:
            level = "시니어" 

    # 전화번호 확인
    if key == "phone":
        phone = "등록"
    else:
        phone = "미등록"

print()
print(f"연령 구간: {level}")
print(f"전화번호: {phone}")


