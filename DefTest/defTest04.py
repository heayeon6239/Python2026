# 파이썬의 함수는 return값을 여러개 받을 때 -> 튜플 사용

def cal(a,b):
    sum_def = a + b
    diff_def = a - b
    return (sum_def, diff_def) # -> 튜플로 묶어서 반환(괄호 있어도되고, 없어도됨)

s,d = cal(10,5) # 합: 15, 차: 5
print(f"합: {s}, 차: {d}")