# 문제 04)

nums = [15, 3, 24, 8, 42, 10]

def find_min_max():
    global max, min
    max = 0
    min = 50
    for num in nums:
        # 최대값
        if num > max:
            max = num
        # 최소값
        if num < min:
            min = num

find_min_max()
print(f"최대값: {max} 최소값: {min}")




