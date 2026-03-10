# 문제2)

# 01. 아이디 입력
while True:
    id = input("아이디 입력 (4~12자): ")
    if len(id) <= 12 and len(id) >= 4:
        # 02. 비밀번호 입력
        while True:
            pw = input("비밀번호 입력 (8자 이상, 숫자 포함): ")
            # ( 8자리 확인 )
            digit = False
            if word >= '0' and word <= '9': # 문자열은 이진수 (숫자) 24,81..
                digit = True
                break
            # ( 숫자포함 확인 )
            if digit:
                for word in pw:
                    if word in ["1","2","3","4","5","6","7","8","9","0"]:
                    
                        # 03. 이메일 입력
                        while True:
                            email = input("이메일 입력: ")
                            # ( @포함 확인 )
                            if "@" in email:
                                print("유효성 검사 통과! API 요청을 전송합니다.")
                                break
                            else:
                                print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.") 

                    else:
                        print("비밀번호는 숫자가 포함되어야 합니다. 다시 입력하세요.") 

            else:
                print("비밀번호는8자 이상이어야 합니다. 다시 입력하세요.")

    else:
        print("아이디는4자 이상12자 이하여야 합니다. 다시 입력하세요.")