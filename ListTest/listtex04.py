# 문제 04)
response = {
    'code' : 200,
    'message': 'success',
    'data' : [
        {'userId': 'user01', 'name': '이자바', 'score': 95},
        {'userId': 'user02', 'name': '박리액트', 'score': 82},
        {'userId': 'user03', 'name': '최스프링', 'score': 91},
        {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
    ]
}

good = []

print("=== 전체 성적 ===")
for res in response.keys():
    if res == "code" and response[res] == 200:
        # 전체 출력
        for one in response['data']:
            print(f"{one['name']} ({one['userId']}): {one['score']}점")
            # 우수 수강생 담기
            if one['score'] >= 90:
                good.append(one)

print(f"=== 우수 수강생 (90점 이상): {len(good)}명 ===")
        
for one in good:
    print(f"★ {one['name']}: {one['score']}점")
