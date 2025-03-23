grades = {
    'A+': 4.5, 'A0': 4.0, 'A': 4.0, 
    'B+': 3.5, 'B0': 3.0, 'B': 3.0,
    'C+': 2.5, 'C0': 2.0, 'C': 2.0,
    'D+': 1.5, 'D0': 1.0, 'D': 1.0,
    'F': 0.0, 'P': None
}

def calculate_gpa(subjects):
    total_points = 0
    total_credits = 0

    for subject_name, grade, credit in subjects:
        if grade not in grades:
            print(f"오류: 유효하지 않은 학점 '{grade}'입니다.")
            continue

        if credit <= 0:
            print(f"오류: 유효하지 않은 학점 수 '{credit}'입니다.")
            continue

        if grade == 'P':
            continue

        total_points += grades[grade] * credit
        total_credits += credit

    if total_credits == 0:
        return 0
    else:
        return round(total_points / total_credits, 2)

subjects = [
    ("미적분학", "A+", 3),
    ("일반물리학", "B0", 4),
    ("자료구조", "A0", 3),
    ("운영체제", "C+", 3),
    ("머신러닝", "B+", 3),
    ("컴퓨터 비전", "B+", 3),
    ("선형대수학", "A", 3),
    ("확률과 통계", "B", 3),
    ("데이터베이스", "C0", 3),
    ("알고리즘", "D+", 3),
    ("인공지능", "F", 3),
    ("객체지향 프로그래밍", "A+", 4),
    ("웹 프로그래밍", "B0", 3),
    ("네트워크", "C+", 3),
    ("소프트웨어 공학", "A0", 3),
    ("디지털 논리 회로", "B+", 3),
    ("임베디드 시스템", "C0", 3),
    ("모바일 프로그래밍", "P", 3),
    ("클라우드 컴퓨팅", "A", 3),
    ("빅데이터 분석", "B", 3)
]

print("최종학점(평점점):", calculate_gpa(subjects))