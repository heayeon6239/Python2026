from datetime import datetime, timedelta

# 문제)
# 기준 날짜 (연체 확인용)
today = '2025-06-10'
# 문자열 -> 날짜로 변환
date_obj = datetime.strptime(today,'%Y-%m-%d')
# 14일 더하기
after_14 = date_obj + timedelta(days=14)

# 도서 목록
books = [
    {'id':'B001','title':'파이썬 완전정복','author':'홍길동','genre':'IT','total':3,'available':3},
    {'id':'B002','title':'데이터분석 입문','author':'김데이터','genre':'IT','total':2,'available':2},
    {'id':'B003','title':'알고리즘의 이해','author':'이알고','genre':'IT','total':2,'available':1},
    {'id':'B004','title':'채식주의자','author':'한강','genre':'소설','total':4,'available':4},
    {'id':'B005','title':'82년생 김지영','author':'조남주','genre':'소설','total':3,'available':3},
]
# 대출 기록
loans = [
    {'loan_id':'L001','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
    {'loan_id':'L002','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]

# 대출 아이디
id = len(loans)

# ------------------------------------------------------------------------------------------------------------------------------

# 1. 도서 목록 출력
def show_books():
    print("도서ID\t제목\t\t저자\t장르\t전체\t가능\t상태")
    print('-'*65)
    for book in books:
        if book["available"] >= 1:
            state = "대출가능"
        else:
            state = "대출불가"
        print(f"{book["id"]}\t{book["title"]}\t{book["author"]}   {book["genre"]}\t{book["total"]}\t{book["available"]}\t{state}")

# 2. 도서 대출
def loan_book():
    name = input("회원명을 입력하세요: ")
    bookId = input("도서ID를 입력하세요: ")

    for book in books:
        # (1) 도서 존재 유무 확인
        if bookId == book["id"]:
            # (2) 도서 대출 가능 확인
            if book["available"] == 0:
                print("현재 대출 가능한 도서가 없습니다.")
            else:
                book['available'] -= 1 # 대출 가능 수량 감소
                list = {'loan_id':f"L{len(loans)+1:03}",'member':name,'book_id':bookId,'loan_date':today,'due_date':today,'returned':False}
                loans.append(list) # 대출 기록에 추가
                print(f"[대출 완료] {name} 님이 '{book['title']}' 을(를) 대출하였습니다.")
                return
    
    print("등록되지 않은 도서입니다.")

# 3. 도서 반납
def return_book():
    id = input("대출번호를 입력하세요: ")
    # (1) 대출번호 존재 유무
    for loan in loans:
        if id == loan["loan_id"]:
            # (2) 이미 반납되었는지 확인
            if loan["returned"] == False:
                # (3) 반납 도서 제목 찾기
                for book in books:
                    if loan["book_id"] == book["id"]:
                        book["available"] += 1 # 대출 가능 수량 증가
                        loan["returned"] = True # 반납상태 변경
                        print(f"[반납 완료] '{book["title"]}' 이(가) 반납되었습니다.")
                        return
            else:
                print("이미 반납된 도서입니다.")
                return
    print("해당 대출 기록이 없습니다.")

# 4. 대출 현황 조회
def show_loans():
    print("대출번호\t회원명\t도서제목\t\t대출일\t반납예정일\t반납여부")
    print("-"*65)
    for loan in loans:
        if loan["returned"] == True:
            returned = "반납완료"
        else:
            returned = "대출중"
        print(f"{loan["loan_id"]:03}\t{loan["member"]}\t{loan["book_id"]}\t\t{loan["loan_date"]}\t{loan["due_date"]}\t{returned}")

# 5. 연체 현황 조회
def show_overdue():
    print(f"=== 연체 현황 (기준일: {today}) ===")
    print("대출번호  회원명\t도서제목\t\t반납예정일")
    print("-"*65)
    for loan in loans:
        # 연체 도서 확인
        if loan["due_date"] < today:
            # 도서 접근
            for book in books:
                if loan["book_id"] == book["id"]:
                    print(f"{loan["loan_id"]}      {loan["member"]}\t{book["title"]}\t\t{loan["due_date"]}")

    print("현재 연체된 도서가 없습니다.")

# 6. 장르별 통계
def show_genre_stats():
    genres = {
        'IT' : {'total':0, 'loan':0},
        '소설' : {'total':0, 'loan':0}
    }

    # 장르별 전체권수
    for book in books:
        genre = genres[book["genre"]] # genre = {'total':0, 'loan':0}
        genre["total"] += book["total"] # 장르별 전체 도서 +1
        # 대출 도서권수
        if book["total"] > book["available"]: 
            loan = book["total"] - book["available"]
            genre["loan"] += loan # 장르별 대출 도서 +1     

    # 출력
    print("장르\t전체권수\t대출중")
    print("-"*65)
    for genre in genres: # 'IT' : {'total':0, 'loan':0}
        # print(genre)
        # print(genres[genre]) # {'total': 3, 'loan': 1}
        one = genres[genre]
        # print(one['total']) # 3,2
        print(f"{genre}\t{one['total']}권\t{one['loan']}권")
    

# ------------------------------------------------------------------------------------------------------------------------------


while True:
    print("=== 도서관 대출 관리 시스템===")
    print("1. 도서 목록 조회")
    print("2. 도서 대출")
    print("3. 도서 반납")
    print("4. 대출 현황 조회")
    print("5. 연체 현황 조회")
    print("6. 장르별 통계")
    print("0. 종료")
    menu = int(input("메뉴를 선택하세요: "))

    # 1. 도서 목록 조회
    if menu == 1:
        show_books()

    # 2. 도서 대출
    elif menu == 2:
        loan_book()

    # 3. 도서 반납
    elif menu == 3:
        show_loans()
        print()
        return_book()

    # 4. 대출 현황 조회
    elif menu == 4:
        show_loans()
    
    # 5. 연체 현황 조회
    elif menu == 5:
        show_overdue()

    # 6. 장르별 통계
    elif menu == 6:
        show_genre_stats()

    # 7. 종료
    else:
        break
        
