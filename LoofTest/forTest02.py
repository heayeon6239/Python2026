# 다중 for문 이용해서 구구단 2단 ~ 9단 출력

for i in range(2,10):
    print(f"-------{i}단-------")
    for q in range(1,11):
        result = i * q
        print(f"{i} × {q} = {result}")
    # 한단이 끝날때마다 출력
    print()