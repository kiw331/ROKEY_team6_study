num = int(input("학생수를 입력하세요\n"))

# 학생수만큼 반복하면서 이름, 국어 영어 수학점수 받기
# input("학생이름, 국어, 영어, 수학점수를 입력하세요")
student_list = []
for i in range(num):                                                
    name, kor, eng, math = input().split()                          # 공백으로 나눠서 이름, 국어, 영어, 수학점수 넣어주기
    student_list.append((name, int(kor), int(eng), int(math)))      # 점수들은 int형 변환 후 넣어주기, ///이름+성적은 튜플형으로 넣어짐      
# print(student_list)   #확인용



# 정렬
# 1.국어 점수가 감소하는 순서로 ->내림
# 2.국어 점수가 같으면 영어 점수가 증가하는 순서로 ->오름
# 3.국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로 ->내림
# 4.모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.) ->오름

#reverse = False
grade_list = sorted(
    student_list,
    key = lambda x: (-x[1], x[2],-x[3], x[0])
)

print("------------------")
for student in grade_list:
    print(student[0])
