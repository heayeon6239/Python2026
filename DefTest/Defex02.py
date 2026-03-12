# 문제 02)

def get_grade(score):
    if score >= 90:
        grade = 'A'
    elif 90 > score >= 80:
        grade = 'B'
    elif 80 > score >= 70:
        grade = 'C'
    else:
        grade = 'F'
    return grade

score_input = int(input("점수를 입력하세요: "))
print(f"학생의 학점은 {get_grade(score_input)}입니다.")



