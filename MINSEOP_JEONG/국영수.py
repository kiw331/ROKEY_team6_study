class Info:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.mat = int(mat)

students = []

# 첫 번째 입력: 학생 수
num_students = int(input('학생 수를 입력하세요. :'))

# 학생 정보 입력 및 저장
for _ in range(num_students):
    name, kor, eng, mat = input().split()
    student = Info(name, kor, eng, mat)
    students.append(student)

# 정렬 기준 설정
students.sort(key=lambda student: (-student.kor, student.eng, -student.mat, student.name))

# 결과 출력
for student in students:
    print(student.name)

