# 문제 05)

menus = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}

def order_coffee(menu, quan=1):
    if menu in menus:
        price = menus[menu] * quan
        return print(f"{menu} {quan}잔 주문 완료. 총액 :{price}")
    else:
        return print(f"{menu}는 메뉴가 없습니다.")

order_coffee("아메리카노")
order_coffee("라떼",3)
order_coffee("녹차")









