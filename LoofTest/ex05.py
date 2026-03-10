# 문제5)

num = int(input("측정 횟수: "))

count = 0
total = 0
max = 0
min = 1000
criticalCnt = 0

while count < num:
    ms = int(input(f"응답시간 {count+1} (ms):"))

    if ms <= 100:
        print("FAST") 
    elif 100 < ms <= 300:
        print("NORMAL") 
    elif 300 < ms <= 1000:
        print("SLOW") 
    elif 1000 < ms:
        print("CRITICAL") 
        criticalCnt += 1
        min = ms
    else:
        print("다시 입력")

    # 전체 응답시간
    total += ms

    # 최대
    if ms > max:
        max = ms

    # 최소
    if ms < min:
        min = ms

    count += 1

# 평균 응답시간
avg = total / num
print(f"평균 응답시간: {avg:.1f}ms")

print(f"최대: {max}ms   | 최소: {min}ms")

if (criticalCnt / num) * 100 > 10:
    print("SLA 위반! 서버 점검이 필요합니다.")