#입력이 0이 될때까지 반복
while True:
    num = input()
    if num == '0':
        break
    
    if num == num[::-1]: #문자열 거꾸로 뒤집는 슬라이싱
        print("yes")
    else:
        print("no")
