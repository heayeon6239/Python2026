# 문제 06)
role_menus = {
    'ADMIN' : ['대시보드', '회원관리', '상품관리', '주문관리', '통계', '시스템설정'],
    'MANAGER': ['대시보드', '상품관리', '주문관리', '통계'],
    'USER' : ['대시보드', '내정보', '주문내역'],
}
# 사용자 목록
users = [
    {'name': '관리자김', 'role': 'ADMIN'},
    {'name': '매니저박', 'role': 'MANAGER'},
    {'name': '일반이', 'role': 'USER'},
    {'name': '일반최', 'role': 'USER'},
]

print("=== 사용자별 접근 메뉴 ===")
# 사용자 목록 접근
# for user in users:
#     if user['role'] == ''
#     print(f"{role_menus[user['role']]}")