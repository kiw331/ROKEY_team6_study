#학생 정보 저장할 리스트
students = []

#학생 정보 입력 받기
for _ in range(int(input())):
    #문자열 분리
    name, korean, english, math = input().split()
    #append() 리스트 끝에 새로운 요소 추가가
    students.append((name, int(korean), int(english), int(math)))

#국어 점수 내림차순
#영어 점수 오름차순
#수학 점수 내림 차순
#이름 오름차순
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0])) 
#국어,영어,수학,이름 순

for student in students:
    print(student[0])
