# 문제 04)
grades = [
    {'id': 1, 'subject': 'Python 프로그래밍', 'score': 92, 'credit': 3},
    {'id': 2, 'subject': 'SpringBoot 개발', 'score': 88, 'credit': 3},
    {'id': 3, 'subject': 'React 프론트엔드', 'score': 76, 'credit': 2},
    {'id': 4, 'subject': '데이터베이스\t', 'score': 95, 'credit': 3},
    {'id': 5, 'subject': '알고리즘\t', 'score': 68, 'credit': 2},
]

creditPoint = 0
totalCredit = 0
total = 0
total01 = 0
dist = {'A+': 0, 'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D': 0}

print("=== 성적표 ===")
print("과목                   점수   학점   학점포인트   이수학점")
print("-"*60)

for grade in grades:
    # 95점 이상 : A+
    if grade['score'] >= 95:
        level, point = "A+", 4.5
        creditPoint += point
        dist['A+'] += 1
    # 90점 이상 : A
    elif 95 > grade['score'] >= 90:
        level, point = "A", 4.0
        creditPoint += point
        dist['A'] += 1
    # 85점 이상 : B+
    elif 90 > grade['score'] >= 85:
        level, point = "B+", 3.5
        creditPoint += point
        dist['B+'] += 1
    # 80점 이상 : B
    elif 85 > grade['score'] >= 80:
        level, point = "B", 3.0
        creditPoint += point
        dist['B'] += 1
    # 75점 이상 : C+
    elif 80 > grade['score'] >= 75:
        level, point = "C+", 2.5
        creditPoint += point
        dist['C+'] += 1
    # 70점 이상 : C
    elif 75 > grade['score'] >= 70:
        level, point = "C", 1.0
        creditPoint += point
        dist['C'] += 1
    # 60점 이상 : D
    elif 70 > grade['score'] >= 60:
        level, point = "D", 1.0
        creditPoint += point
        dist['D'] += 1
    # 60점 미만 : F
    else:
        level, point = "F", 0
        creditPoint += point
    
    # grades 리스트에 추가 ★
    grade['level'] = level
    grade['point'] = point


    # F제외한 이수학점 총계
    if grade['score'] >= 60:
         totalCredit += grade['credit']
         total = grade['credit'] * point

    # 각 과목별(학점포인트*이수학점) 총합
    total01 += total

    # 출력
    print(f"{grade['subject']} \t {grade['score']}점 \t {level} \t {point} \t {grade['credit']}학점")


# GPA 계산
gpa = total01 / totalCredit

print()
print(f"GPA: {gpa:.2f} / 4.50 (총 {totalCredit}학점)")

# 학점분포 (1)
# di = {}
# for i in dist.keys():
#     if dist[i] != 0:
#         di[i] = dist[i]

# print(f"학점분포: {di}")

# 학점분포 (2) ★★★★★
di = {}
for g in grades:
    grade = g['level'] # grades 리스트에서 key값이 level인 값을 하나씩 grade에 담음 ex) 'A'
    # 이미 학점이 존재하면 +1, 아니면 1
    if grade in di:
        di[grade] += 1
    else:
        di[grade] = 1
        
# print(f"학점분포: {di}")
print("학점분포:",di)



