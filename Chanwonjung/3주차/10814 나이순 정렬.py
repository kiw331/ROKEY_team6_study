#회원 수 입력 받기
num = int(input())

#회원 정보 리스트로 저장
members = []

#회원 정보 입력 받기
for i in range(num):
    age, name = input().split()
    age = int(age)
    members.append((age, name))

#나이 기준으로 정렬
sort_members = sorted(members, key=lambda x:x[0])

for member in sort_members:
    print(member[0], member[1])