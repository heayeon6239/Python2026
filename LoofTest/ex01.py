# 문제 1)

code = int(input("상태코드를 입력하세요: "))

if code in [200,201]:
    note = "2xx 성공"
    if code == 200:
        stateNote = "OK - 요청 성공"
    else:
        stateNote = "Created - 리소스 생성 성공"
elif code in [400,401,403,404]:
    note = "4xx 클라이언트 오류"
    if code == 400:
        stateNote = "Bad Request - 잘못된 요청"
    elif code == 401:
        stateNote = "Unauthorized - 인증 필요"
    elif code == 403:
        stateNote = "Forbidden - 접근 권한 없음"
    else:
        stateNote = "Not Found - 리소스 없음"
elif code == 500:
    note = "5xx 서버오류"
    stateNote = "Internal Server Error - 서버 내부 오류"

print(f"상태: {code} {stateNote}")
print(f"계열: {note}")