# 문제3)

selectquan = 0
insertquan = 0
updatequan = 0
deletequan = 0

while True:
    # .upper() => 소문자를 입력해도 대문자로 출력
    # .lower() => 대문자를 입력해도 소문자로 출력
    queryType = input("쿼리 유형 입력: ").upper()

    if queryType == "SELECT":
        selectquan += 1 
    elif queryType == "INSERT":
        insertquan += 1
    elif queryType == "UPDATE":
        updatequan += 1
    elif queryType == "DELETE":
        deletequan += 1
    # elif queryType == "REPORT":
    #     total = selectquan + insertquan + updatequan + deletequan
    #     print(f"SELECT : {selectquan}회")
    #     print(f"INSERT : {insertquan}회")
    #     print(f"UPDATE : {updatequan}회")
    #     print(f"DELETE : {deletequan}회")
    #     print(f"총 실행 : {total}회")
        
    elif queryType == "EXIT":
        # select문이 70% 이상일 경우
        total = selectquan + insertquan + updatequan + deletequan
        print((selectquan / total) * 100)
        if total != 0:
            if  (selectquan / total) * 100 >= 70:
                print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")
                break
            else:
                print(f"SELECT : {selectquan}회")
                print(f"INSERT : {insertquan}회")
                print(f"UPDATE : {updatequan}회")
                print(f"DELETE : {deletequan}회")
                print(f"총 실행 : {total}회")
                break
        else:
            print(f"SELECT : {selectquan}회")
            print(f"INSERT : {insertquan}회")
            print(f"UPDATE : {updatequan}회")
            print(f"DELETE : {deletequan}회")
            print(f"총 실행 : {total}회")
            break
    else:
        print("알 수 없는 쿼리 유형입니다.")