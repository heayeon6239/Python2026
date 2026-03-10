# 문제 7)

pw = input("비밀번호 입력: ")

ok00 = 'X'
ok01 = 'X'
ok02 = 'X'
ok03 = 'X'
ok04 = 'X'

cnt00 = 0
cnt01 = 0
cnt02 = 0
cnt03 = 0
cnt04 = 0

# 길이 8자 이상 확인
if len(pw) >= 8:
    ok00 = 'O'
    cnt00 = 1

for ch in pw:
    # 대문자 포함 여부
    if ch >= 'A' and ch <= 'Z':
        ok01 = 'O'
        cnt01 = 1
    # 소문자 포함 여부
    elif ch >= 'a' and ch <= 'z':
        ok02 = 'O'
        cnt02 = 1
    # 숫자 포함 여부
    elif ch >= '0' and ch <= '9':
        ok03 = 'O'
        cnt03 = 1
    # 특수문자 포함 여부(위4가지에 해당하지 않는 문자)
    else:
        ok04 = 'O'
        cnt04 = 1

cnt = cnt00 + cnt01 + cnt02 + cnt03 + cnt04

if cnt == 5:
    note = "매우 강함"
else:
    note = "취약 X"


print(f"[{ok00}] 길이 8자 이상")
print(f"[{ok01}] 대문자 포함")
print(f"[{ok02}] 소문자 포함")
print(f"[{ok03}] 숫자 포함")
print(f"[{ok04}] 특수문자 포함")
print(f"비밀번호 강도: {note}")