# 문제 9)

ok = 0
cnt = 0
no = ""
answers = [
       "DB 마이그레이션 완료 여부", 
       "application-prod.properties 설정 확인",
       "JWT Secret Key 변경 여부",
       "CORS 허용 도메인 설정 완료",
       "API 엔드포인트 테스트 통과"
        ]

for answer in answers:
    # 질문
    ans = input(f"[{cnt+1}/5] {answer}(Y/N): ").upper()

    if ans == "Y":
        print("-> 완료")
    else:
        print("-> 미완료")
        no += f"[{cnt}] {answer}\n"
        ok += 1
    
    cnt += 1

# 모든 항목 통과
if ok == 5:
    print("배포 승인! 배포를 진행하세요.")
else:
    print(f"배포 보류! {ok}개 항목을 해결 후 재시도하세요")
    print(no)
