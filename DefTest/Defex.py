# 총 복습 문제)
rooms = [
    {'id': 101, 'name':'스탠다드 A' , 'price': 100000, 'max': 2, 'state': True},
    {'id': 102, 'name':'스탠다드 B' , 'price': 110000, 'max': 2, 'state': True},
    {'id': 201, 'name':'디럭스 룸' , 'price': 250000, 'max': 4, 'state': True},
    {'id': 301, 'name':'스위트 룸' , 'price': 500000, 'max': 6, 'state': False},
    ]
reservations = [] # 삭제까지 포함한 모든 예약내역(튜플)
reservationList = [] # 예약내역

# 전체 객실 목록
def show_rooms(only_available = False):
    global allRoom
    allRoom = []
    for room in rooms:
        # 예약 가능한 객실만 출력
        if only_available == True:
            if room['state'] == True:
                allRoom.append(room)
        # 전체 출력
        else:
            allRoom.append(room)

# 객실 예약
def make_reservation(res_list, room_id, quest_name, day, people):
    for res in res_list:
        # 예약 가능
        if room_id == res["id"]:
                res["state"] = False

                # 총액 계산
                totalPrice = calculate_price(room_id, day, people)

                # 튜플상태로 배열에 담음
                resData = (room_id, quest_name, people, totalPrice) # 튜플로 만들기
                reservations.append(resData)
                # 수정가능한 배열에 담음
                res["quest_name"] = quest_name
                res["room"] = room_id
                res["people"] = people
                res["price"] = totalPrice
                reservationList.append(res)
                return "예약이 완료되었습니다."
        
    # 예약 불가능
    return "예약이 불가능합니다."

# 총액 계산
def calculate_price(room_id, days, people):
    for room in rooms:
        if room_id == room["id"]:
            price = room["price"] * days
            # 인원 초과
            if people > room["max"]:
                plus = people - room["max"] # 추가인원
                extra = plus * 20000 # 추가금액
                return price + extra
            else:
                return price
            
# 삭제
def cancel_reservation(room_id):
    for room in reservationList:
        if room_id == room["id"]:
            reservationList.remove(room)
    for room in rooms:
        if room_id == room["id"]:
            room["state"] = False
            

# ---------------------------------------- 출력용 --------------------------------------------

# 객실 출력용(전체or예약가능)
def showList(only_available = False):
    show_rooms(only_available)
    print("=" * 60)
    print("ID   객실명\t\t가격\t  최대인원      상태")
    print("-" * 60)
    for room in allRoom:
        if room["state"] == True:
            ok = "예약가능"
        else:
            ok = "예약불가"
        print(f"{room["id"]}  {room["name"]}\t\t{room["price"]}\t     {room["max"]}\t\t{ok}")

# 예약 내역 출력용
def reservationPrint():
    for res in reservationList:
        print(f"성함: {res["quest_name"]} | 객실번호: {res["id"]}호 | 인원: {res["people"]}명 | 가격: {res["price"]}")
    
    
# 총 매출액 출력용
def totalPrice():
    total = 0
    for res in reservationList:
        total += res["price"]
    return total

        
while True:
    print()
    print("--- 리조트 예약 관리 시스템 ---")
    print("1. 객실 현황 보기")
    print("2. 객실 예약하기")
    print("3. 예약 내역 및 매출 확인")
    print("4. 삭제")
    print("5. 프로그램 종료")
    menu = int(input("5. 원하는 메뉴 번호를 선택하세요: "))
    print()

    # 1. 객실 현황 보기
    if menu == 1:
        showList() # 전체 객실 출력
    
    # 2. 객실 예약하기
    elif menu == 2:
        showList(True) # 예약 가능 객실 출력
        print()
        roomId = int(input("예약할 객실 ID를 입력하세요: "))
        name = input("예약자 성함을 입력하세요: ")
        day = int(input("숙박일수를 입력하세요: "))
        p_num = int(input("투숙 인원을 입력하세요 (최대 4명): "))
        print(make_reservation(allRoom,roomId,name,day,p_num))
        print(reservationList)

    # 3. 예약 내역 및 매출 확인
    elif menu == 3:
        print("--- 전체 예약 명단 ---")
        reservationPrint()
        print()
        print(f"현재 확정 매출 합계: {totalPrice():,}원")

    # 4. 예약 삭제
    elif menu == 4:
        del_room = int(input("삭제할 객실 아이디를 입력하세요: "))
        cancel_reservation(del_room)

    # 5. 프로그램 종료
    else:
        print("프로그램 종료")
        break


        
    












