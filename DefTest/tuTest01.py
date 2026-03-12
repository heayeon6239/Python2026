# 튜플 : 여러개의 데이터를 순서대로 저장 (단, 수정/삭제/추가 안됨)
# a = (10, 20, 30)

# 01. 튜플접근 => a[0]
a = (10, 20, 30)
# a[0] = 15 -> 수정불가
print(a[0]) # 10

# 02.
fruit = ('apple', 'banana', 'orange')
for f in fruit:
    print(f, end=" ") # apple banana orange

print()

# 03.
if 'abce' in fruit: # X
    print("O")
else:
    print("X")

# 04. 튜플은 괄호()가 없어도 됨
t = 10,20,30
print(t) # (10, 20, 30)

print()

# 문제) 주어진 자료를 이용하여 합계, 평균구하기
score = (80, 50, 75, 90)
total = 0
for sco in score:
    total += sco
avg = total / len(score)
print(total) # 295
print(avg) # 73.75
