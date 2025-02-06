def minimize_expression(expression):
    # '-'를 기준으로 수식을 분리
    parts = expression.split('-')
    
    # 첫 번째 부분은 무조건 더하기
    result = sum(map(int, parts[0].split('+')))
    
    # 나머지 부분은 괄호로 묶어서 빼기
    for part in parts[1:]:
        result -= sum(map(int, part.split('+')))
    
    return result

# 입력 받기
expression = input().strip()
print(minimize_expression(expression))
