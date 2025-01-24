while (1) :     # 무한 루프 
    num = input()   # 정수 입력   
    if num == '0':    # 0이 입력되면 while문 탈출
        break

    # 숫자열과 숫자열을 뒤집은 값을 비교
    elif num == num[::-1]: 
        print('yes')
    else:
        print('no')
    
        