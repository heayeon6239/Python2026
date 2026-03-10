# 문제 9)

ok = 0
cnt = 0
answers = [
       "DB 마이그레이션 완료 여부", 
       "application-prod.properties 설정 확인",
       "JWT Secret Key 변경 여부",
       "CORS 허용 도메인 설정 완료",
       "API 엔드포인트 테스트 통과"
        ]

for ans in answers:
    # 질문
    ans = input(f"[{cnt+1}/5] {ans}(Y/N): ").upper()

    if ans == "Y":
        print("-> 완료")
        ok += 1
    else:
        print("-> 미완료")
        no = cnt

# 모든 항목 통과
if ok == 5:
    print("배포 승인! 배포를 진행하세요.")
