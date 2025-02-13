import sys

try:
    nums = sys.stdin.readline().strip() #입력을 받아 양 끝 공백 제거

    #'-'을 기준으로 분할하여
    #식의 값을 최소로 만듦.
    #ex) 55-50+40 -> [55,50+40]
    min_nums = nums.split('-')

    #분할 이후 가장 앞 숫자 그룹은 모두 더함
    #ex)55-50+40 에서 55만 더해지므로 result = 55
    result = sum(map(int, min_nums[0].split('+'))) if min_nums[0] else 0

    #이후 부분들은 내부적으로 더한 뒤 result 값에서 빼줌
    #ex) min_nums[1:] = [50+40]
    #ex) 50+40.split -> 50, 40
    #ex) sum(map(int, [50, 40])) -> 50 + 40 = 90이므로 result -= 90
    #ex) result = 55 - 90 = -35
    for min_num in min_nums[1:]:
        result -= sum(map(int, min_num.split('+'))) if min_num else 0

    print(result)

except Exception as e:
    print("Error", e)