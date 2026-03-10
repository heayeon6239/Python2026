# 문제) 1부터 50까지 합을 구하라(while문 이용)

num = 1
result = 0
while num <= 50:
    result += num
    num += 1
print(result)

# 다중 while문을 이용해서 구구단 2단 ~ 9단 출력

i = 2
while i <= 9:
    print(f"------{i}단------")
    q = 1
    while q <= 10:
        result = i * q
        print(f"{i} × {q} = {result}")
        q += 1
    print()
    i += 1